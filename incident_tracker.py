from enum import Enum


class AlertType(Enum):
    LOGIN_FAILURE = "login_failure"
    LOGIN_SUCCESS = "login_success"
    FILE_HASH_DETECTED = "file_hash_detected"
    DNS_QUERY = "dns_query"
    PORT_SCAN = "port_scan"


class Alert:
    def __init__(self, date, alert_type, asset, indicator):
        self.date = date
        self.alert_type = alert_type
        self.asset = asset
        self.indicator = indicator
        self.classification = self._classify_indicator()

    def __str__(self):
        return (
            f"{self.date} [{self.severity()}] "
            f"{self.alert_type.value} on {self.asset} -> {self.indicator}"
        )

    def severity(self):
        if self.alert_type == AlertType.FILE_HASH_DETECTED:
            return "HIGH"
        elif self.alert_type in (AlertType.PORT_SCAN, AlertType.DNS_QUERY):
            return "MEDIUM"
        return "LOW"

    def _classify_indicator(self):
        ind = self.indicator
        if ind.startswith(("10.", "192.168.")):
            return "internal"
        if "." in ind and any(ch.isdigit() for ch in ind):
            return "external"
        return "N/A"


alerts = []

with open("alerts.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

print(f"Loaded {len(lines)} alerts.\n")

for line in lines:
    if not line.strip():
        continue
    date, alert_type_str, asset, indicator = line.split(",")
    alert_type = AlertType(alert_type_str)
    alert = Alert(date, alert_type, asset, indicator)
    alerts.append(alert)


high = 0
medium = 0
low = 0
internal = 0
external = 0
na = 0

report_lines = [
    "Incident Triage Summary",
    "=" * 40,
    "",
]

for alert in alerts:
    sev = alert.severity()

    if sev == "HIGH":
        high += 1
    elif sev == "MEDIUM":
        medium += 1
    else:
        low += 1

    if alert.classification == "internal":
        internal += 1
    elif alert.classification == "external":
        external += 1
    else:
        na += 1

    report_lines.append(str(alert))
    report_lines.append(f"   Classification: {alert.classification}")
    report_lines.append("")

report_lines.extend([
    "=" * 40,
    f"Total alerts processed: {len(alerts)}",
    f"HIGH:   {high}",
    f"MEDIUM: {medium}",
    f"LOW:    {low}",
    f"Internal: {internal} | External: {external} | N/A: {na}",
])

report_text = "\n".join(report_lines)
print(report_text)

with open("incident_summary.txt", "w", encoding="utf-8") as out:
    out.write(report_text)

print("\n✅ Report saved to incident_summary.txt")