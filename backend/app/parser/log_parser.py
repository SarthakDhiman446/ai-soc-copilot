import re


class LogParser:

    @staticmethod
    def parse_log(filepath: str):

        parsed_events = []

        with open(filepath, "r", encoding="utf-8") as file:

            for line in file:

                event = {
                    "raw_log": line.strip(),
                    "event_type": "Unknown",
                    "severity": "Low",
                    "ip_address": None,
                }

                # Extract IP Address
                ip_match = re.search(
                    r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
                    line
                )

                if ip_match:
                    event["ip_address"] = ip_match.group()

                # Failed Login
                if "failed" in line.lower():

                    event["event_type"] = "Failed Login"
                    event["severity"] = "Medium"

                # Successful Login
                elif "accepted" in line.lower():

                    event["event_type"] = "Successful Login"
                    event["severity"] = "Low"

                parsed_events.append(event)

        return parsed_events