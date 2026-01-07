QUALITY_GATE = {
    "min_pass_rate": 95,
    "max_critical_defects": 0
}

def release_approved(metrics: dict) -> bool:
    if metrics["pass_rate"] < QUALITY_GATE["min_pass_rate"]:
        return False
    if metrics["critical_defects"] > QUALITY_GATE["max_critical_defects"]:
        return False
    return True

if __name__ == "__main__":
    metrics = {
        "pass_rate": 97,
        "critical_defects": 0
    }

    print("RELEASE APPROVED" if release_approved(metrics) else "RELEASE BLOCKED")
