class TimelineService:

    @staticmethod
    def build(events):

        timeline = []

        for index, event in enumerate(events, start=1):

            timeline.append({
                "step": index,
                "event": event["event_type"],
                "severity": event["severity"],
                "ip": event["ip_address"]
            })

        return timeline