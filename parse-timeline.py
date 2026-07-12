#!/usr/bin/env python3
"""
Google Timeline Parser - Complete Version for Semantic Segments (With Statistics)
Properly parses modern Google Takeout Semantic Segments with accurate GPS,
distance tracking, and deep movement statistics.
"""

import argparse
import json
import math
import os
import csv
from collections import defaultdict
from datetime import datetime, timedelta


class TimelineEditsParser:
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.semantic_segments = []

    def load_timeline_edits(self, file_path=None):
        """Load ALL semantic segments from JSON file(s)"""
        if file_path:
            self.file_path = file_path

        if not self.file_path:
            raise ValueError("No file path provided")

        total_segments = 0

        if os.path.isfile(self.file_path):
            total_segments += self._load_single_file(self.file_path)
        elif os.path.isdir(self.file_path):
            json_files = []
            for root, dirs, files in os.walk(self.file_path):
                for file in files:
                    if file.endswith(".json") and ("timeline" in file.lower() or "segments" in file.lower()):
                        json_files.append(os.path.join(root, file))

            print(f"Found {len(json_files)} timeline JSON files")
            for fp in json_files:
                count = self._load_single_file(fp)
                total_segments += count
                print(f"  {os.path.basename(fp)}: {count} segments")
        else:
            print(f"Error: {self.file_path} is not a valid file or directory!")
            return False

        print(f"Total loaded: {total_segments} semantic segments")
        return True

    def _load_single_file(self, file_path):
        """Load segments from a single JSON file"""
        count = 0
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                if "semanticSegments" in data:
                    self.semantic_segments.extend(data["semanticSegments"])
                    count = len(data["semanticSegments"])
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

        return count

    def _clean_lat_lng(self, coord_str):
        """Extract float components from a '52.1234°, 8.1234°' string format"""
        if not coord_str:
            return None, None
        try:
            parts = coord_str.replace("°", "").split(",")
            return float(parts[0].strip()), float(parts[1].strip())
        except Exception:
            return None, None

    def parse_all_signals(self):
        """Parse modern semantic segments layout into activity-like and position structures"""
        activities = []
        positions = []
        wifi_scans = []

        print("Parsing timeline segments...")

        for i, segment in enumerate(self.semantic_segments):
            device_id = "takeout_device"
            start_time_str = segment.get("startTime", "")
            end_time_str = segment.get("endTime", "")

            start_dt, end_dt = None, None
            try:
                if start_time_str:
                    start_dt = datetime.fromisoformat(start_time_str.replace("Z", "+00:00"))
                if end_time_str:
                    end_dt = datetime.fromisoformat(end_time_str.replace("Z", "+00:00"))
            except Exception:
                continue

            # Fall 1: timelinePath
            if "timelinePath" in segment:
                for idx, path_point in enumerate(segment["timelinePath"]):
                    point_time_str = path_point.get("time", start_time_str)
                    try:
                        p_dt = datetime.fromisoformat(point_time_str.replace("Z", "+00:00"))
                    except Exception:
                        p_dt = start_dt

                    lat, lng = self._clean_lat_lng(path_point.get("point", ""))
                    if lat and lng:
                        positions.append({
                            "edit_index": i,
                            "timestamp": p_dt,
                            "device_id": device_id,
                            "signal_type": "position",
                            "latitude": lat,
                            "longitude": lng,
                            "lat_e7": int(lat * 1e7),
                            "lng_e7": int(lng * 1e7),
                            "accuracy_m": 15.0,
                            "source": "TIMELINE_PATH",
                        })

            # Fall 2: activity
            if "activity" in segment:
                act = segment["activity"]
                top_candidate = act.get("topCandidate", {})
                act_type = top_candidate.get("type", "UNKNOWN_ACTIVITY")
                prob = top_candidate.get("probability", act.get("probability", 1.0))

                lat, lng = self._clean_lat_lng(act.get("start", {}).get("latLng", ""))
                if lat and lng:
                    activities.append({
                        "edit_index": i,
                        "timestamp": start_dt,
                        "device_id": device_id,
                        "signal_type": "activity",
                        "primary_activity": f"START_{act_type}",
                        "primary_probability": prob,
                        "all_activities": [top_candidate],
                        "latitude": lat,
                        "longitude": lng,
                        "accuracy_m": 20.0,
                    })

                lat_end, lng_end = self._clean_lat_lng(act.get("end", {}).get("latLng", ""))
                if lat_end and lng_end:
                    activities.append({
                        "edit_index": i,
                        "timestamp": end_dt,
                        "device_id": device_id,
                        "signal_type": "activity",
                        "primary_activity": f"END_{act_type}",
                        "primary_probability": prob,
                        "all_activities": [top_candidate],
                        "latitude": lat_end,
                        "longitude": lng_end,
                        "accuracy_m": 20.0,
                    })

            # Fall 3: visit
            elif "visit" in segment:
                visit = segment["visit"]
                top_candidate = visit.get("topCandidate", {})
                place_id = top_candidate.get("placeId", "UNKNOWN_PLACE")
                prob = top_candidate.get("probability", visit.get("probability", 1.0))

                lat, lng = self._clean_lat_lng(top_candidate.get("placeLocation", {}).get("latLng", ""))
                if lat and lng:
                    activities.append({
                        "edit_index": i,
                        "timestamp": start_dt,
                        "device_id": device_id,
                        "signal_type": "activity",
                        "primary_activity": f"VISIT_START_{place_id[:10]}",
                        "primary_probability": prob,
                        "all_activities": [{"placeId": place_id}],
                        "latitude": lat,
                        "longitude": lng,
                        "accuracy_m": 10.0,
                    })

            # Fall 4: position
            elif "position" in segment:
                pos = segment["position"]
                pos_time_str = pos.get("timestamp", start_time_str)
                try:
                    p_dt = datetime.fromisoformat(pos_time_str.replace("Z", "+00:00"))
                except Exception:
                    p_dt = start_dt

                lat, lng = self._clean_lat_lng(pos.get("LatLng", ""))
                if lat and lng:
                    positions.append({
                        "edit_index": i,
                        "timestamp": p_dt,
                        "device_id": device_id,
                        "signal_type": "position",
                        "latitude": lat,
                        "longitude": lng,
                        "lat_e7": int(lat * 1e7),
                        "lng_e7": int(lng * 1e7),
                        "accuracy_m": float(pos.get("accuracyMeters", 10)),
                        "source": pos.get("source", "RAW_POSITION"),
                    })

        print(f"Parsed {len(activities)} activity/visit markers, {len(positions)} position records.")
        return activities, positions, wifi_scans

    def correlate_activities_with_positions(self, activities, positions):
        """Merges and aligns activities and track points chronologically"""
        print("Correlating records...")
        enhanced_records = []

        for act in activities:
            rec = act.copy()
            rec["lat_e7"] = int(act["latitude"] * 1e7) if act.get("latitude") else None
            rec["lng_e7"] = int(act["longitude"] * 1e7) if act.get("longitude") else None
            rec["gps_source"] = "SEGMENT_ENDPOINT"
            rec["time_to_gps"] = 0
            enhanced_records.append(rec)

        for pos in positions:
            enhanced_records.append({
                "edit_index": pos["edit_index"],
                "timestamp": pos["timestamp"],
                "device_id": pos["device_id"],
                "signal_type": "position_only",
                "primary_activity": "GPS_POINT",
                "primary_probability": 1.0,
                "latitude": pos["latitude"],
                "longitude": pos["longitude"],
                "lat_e7": pos["lat_e7"],
                "lng_e7": pos["lng_e7"],
                "accuracy_m": pos["accuracy_m"],
                "gps_source": pos["source"],
                "time_to_gps": 0,
                "all_activities": [],
            })

        enhanced_records.sort(key=lambda x: x["timestamp"])
        print(f"Created {len(enhanced_records)} timeline entries.")
        return enhanced_records

    def haversine_distance(self, lat1, lon1, lat2, lon2):
        """Calculate the great circle distance between two points on Earth (in meters)"""
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        return c * 6371000

    def analyze_enhanced_data(self, enhanced_records):
        print(f"\n=== ENHANCED TIMELINE ANALYSIS ===")
        print(f"Total records: {len(enhanced_records)}")

        if not enhanced_records:
            print("No data to analyze")
            return

        start_date = enhanced_records[0]["timestamp"].strftime("%Y-%m-%d %H:%M")
        end_date = enhanced_records[-1]["timestamp"].strftime("%Y-%m-%d %H:%M")
        total_hours = (enhanced_records[-1]["timestamp"] - enhanced_records[0]["timestamp"]).total_seconds() / 3600
        print(f"Data period: {start_date} to {end_date} ({total_hours:.1f} hours)")

        # Activity analysis
        activity_counts = defaultdict(int)
        gps_quality_stats = {"with_gps": 0, "without_gps": 0, "total_accuracy": 0, "gps_count": 0}

        for record in enhanced_records:
            activity = record.get("primary_activity", "UNKNOWN")
            activity_counts[activity] += 1

            if record.get("latitude") and record.get("longitude"):
                gps_quality_stats["with_gps"] += 1
                accuracy = record.get("accuracy_m", 0)
                if accuracy > 0:
                    gps_quality_stats["total_accuracy"] += accuracy
                    gps_quality_stats["gps_count"] += 1
            else:
                gps_quality_stats["without_gps"] += 1

        print(f"\n=== ACTIVITY SUMMARY ===")
        total_records = len(enhanced_records)
        for activity, count in sorted(activity_counts.items(), key=lambda x: x[1], reverse=True)[:15]:
            percentage = (count / total_records) * 100
            print(f"{activity}: {count} records ({percentage:.1f}%)")

        print(f"\n=== GPS DATA QUALITY ===")
        print(f"Records with GPS: {gps_quality_stats['with_gps']}/{total_records} ({gps_quality_stats['with_gps'] / total_records * 100:.1f}%)")
        print(f"Records without GPS: {gps_quality_stats['without_gps']}")

        if gps_quality_stats["gps_count"] > 0:
            avg_accuracy = gps_quality_stats["total_accuracy"] / gps_quality_stats["gps_count"]
            print(f"Average GPS accuracy: {avg_accuracy:.0f} meters")

        # Re-introducing original Movement analysis engine
        self.analyze_movement_with_gps(enhanced_records)

    def analyze_movement_with_gps(self, enhanced_records):
        """Analyze movement patterns using GPS data (Restored Feature)"""
        print(f"\n=== MOVEMENT ANALYSIS WITH GPS ===")

        # Filter records with valid GPS data and safe accuracy bounds
        gps_records = [
            r for r in enhanced_records 
            if r.get("latitude") and r.get("longitude") and r.get("accuracy_m", 1000) < 100
        ]

        if len(gps_records) < 2:
            print("Not enough GPS data for movement analysis")
            return

        print(f"Using {len(gps_records)} GPS records for movement analysis")

        total_distance = 0
        movements = []

        for i in range(1, len(gps_records)):
            prev_record = gps_records[i - 1]
            curr_record = gps_records[i]

            distance = self.haversine_distance(
                prev_record["latitude"], prev_record["longitude"],
                curr_record["latitude"], curr_record["longitude"],
            )

            time_diff = (curr_record["timestamp"] - prev_record["timestamp"]).total_seconds()

            # Filter signal noise (distance > 5m, time window < 1h)
            if distance > 5 and time_diff > 0 and time_diff < 3600:
                speed = distance / time_diff  # m/s

                if speed < 50:  # ~180 km/h limit to remove teleportation jumps
                    total_distance += distance

                    movements.append({
                        "timestamp": curr_record["timestamp"],
                        "distance": distance,
                        "time_diff": time_diff,
                        "speed_ms": speed,
                        "speed_kmh": speed * 3.6,
                        "activity": curr_record.get("primary_activity", "UNKNOWN"),
                        "start_lat": prev_record["latitude"],
                        "start_lng": prev_record["longitude"],
                        "end_lat": curr_record["latitude"],
                        "end_lng": curr_record["longitude"],
                    })

        if movements:
            print(f"Total distance traveled: {total_distance:.0f} meters ({total_distance / 1000:.2f} km)")
            print(f"Number of movements: {len(movements)}")

            # Speed analysis by activity
            activity_speeds = defaultdict(list)
            for movement in movements:
                activity_speeds[movement["activity"]].append(movement["speed_kmh"])

            print(f"\nSpeed analysis by activity:")
            for activity, speeds in activity_speeds.items():
                if speeds:
                    avg_speed = sum(speeds) / len(speeds)
                    max_speed = max(speeds)
                    print(f"  {activity}: avg {avg_speed:.1f} km/h, max {max_speed:.1f} km/h ({len(speeds)} movements)")

            # Show top movements
            print(f"\nTop 10 longest movements:")
            top_movements = sorted(movements, key=lambda x: x["distance"], reverse=True)[:10]
            for i, movement in enumerate(top_movements, 1):
                time_str = movement["timestamp"].strftime("%Y-%m-%d %H:%M")
                distance = movement["distance"]
                speed = movement["speed_kmh"]
                activity = movement["activity"]
                print(f"  {i}. {time_str}: {distance:.0f}m at {speed:.1f} km/h ({activity})")
        else:
            print("No significant movements detected")

    def export_enhanced_csv(self, enhanced_records, filename="Timeline-enhanced.csv"):
        """Export enhanced data into expected format structure"""
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "timestamp", "date", "time", "primary_activity", "probability",
                "latitude", "longitude", "lat_e7_original", "lng_e7_original",
                "distance_to_prev_meters", "accuracy_m", "gps_source",
                "time_to_gps_seconds", "device_id", "signal_type", "all_activities_json"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            prev_lat, prev_lng = None, None

            for record in enhanced_records:
                timestamp = record["timestamp"]
                current_lat = record.get("latitude")
                current_lng = record.get("longitude")

                distance_to_prev = ""
                if current_lat and current_lng:
                    if prev_lat is not None and prev_lng is not None:
                        distance = self.haversine_distance(prev_lat, prev_lng, current_lat, current_lng)
                        distance_to_prev = f"{distance:.1f}"
                    else:
                        distance_to_prev = "0.0"
                    prev_lat, prev_lng = current_lat, current_lng

                lat_str = f"{current_lat:.7f}" if current_lat else ""
                lng_str = f"{current_lng:.7f}" if current_lng else ""

                writer.writerow({
                    "timestamp": timestamp.isoformat(),
                    "date": timestamp.strftime("%Y-%m-%d"),
                    "time": timestamp.strftime("%H:%M:%S"),
                    "primary_activity": record.get("primary_activity", ""),
                    "probability": record.get("primary_probability", ""),
                    "latitude": lat_str,
                    "longitude": lng_str,
                    "lat_e7_original": record.get("lat_e7", ""),
                    "lng_e7_original": record.get("lng_e7", ""),
                    "distance_to_prev_meters": distance_to_prev,
                    "accuracy_m": record.get("accuracy_m", ""),
                    "gps_source": record.get("gps_source", ""),
                    "time_to_gps_seconds": record.get("time_to_gps", ""),
                    "device_id": record.get("device_id", ""),
                    "signal_type": record.get("signal_type", ""),
                    "all_activities_json": json.dumps(record.get("all_activities", [])),
                })

        print(f"\nEnhanced CSV successfully generated: {filename}")

    def filter_by_date(self, enhanced_records, date_filter):
        if not date_filter:
            return enhanced_records
        print(f"Filtering data for: {date_filter}")
        filtered = []
        for r in enhanced_records:
            ts_str = r["timestamp"].strftime("%Y-%m-%d")
            if ts_str.startswith(date_filter):
                filtered.append(r)
        print(f"Filtered to {len(filtered)} records")
        return filtered


def main():
    parser = argparse.ArgumentParser(description="Parse Google Semantic Segments JSON Data with Movement Analytics")
    parser.add_argument("path", help="Path to Timeline JSON file or directory")
    parser.add_argument("--export-csv", action="store_true", help="Export to CSV file with tracking features")
    parser.add_argument("--date-filter", help="Filter by date (YYYY-MM-DD or YYYY-MM)", default=None)

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: Path {args.path} not found!")
        return

    print("Google Timeline Parser (Semantic Segments Engine + Full Stats)")
    print("==========================================================")

    parser_instance = TimelineEditsParser(args.path)

    if not parser_instance.load_timeline_edits():
        return

    activities, positions, _ = parser_instance.parse_all_signals()
    enhanced_records = parser_instance.correlate_activities_with_positions(activities, positions)

    if args.date_filter:
        enhanced_records = parser_instance.filter_by_date(enhanced_records, args.date_filter)

    parser_instance.analyze_enhanced_data(enhanced_records)

    if args.export_csv:
        parser_instance.export_enhanced_csv(enhanced_records)


if __name__ == "__main__":
    main()