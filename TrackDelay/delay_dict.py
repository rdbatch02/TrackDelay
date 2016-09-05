def to_delay_dict(record):
    delay_dict = {}
    delay_dict["alert_id"] = record["alert_id"]
    delay_dict["severity"] = record["severity"]
    line_components = record["effected_services"]["services"][0]["route_id"].split('-')
    delay_dict["line"] = line_components[0]
    delay_dict["branch"] = line_components[1] if len(line_components) > 1 else None
    delay_dict["start_time"] = record["effect_periods"][0]["effect_start"] if len(record["effect_periods"]) > 1 else record["created_dt"]
    delay_dict["end_time"] = record["effect_periods"][0]["effect_end"] if len(record["effect_periods"]) > 1 else None
    delay_dict["header_text"] = record["header_text"]
    delay_dict["descr_text"] = record["description_text"]