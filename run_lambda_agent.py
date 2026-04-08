import os
import json
from anthropic import Anthropic
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
def detect_anomaly(record):
    baseline = record["baseline_cost"]
    current = record["current_cost"]

    variance = current - baseline
    variance_pct = (variance / baseline) * 100

    is_anomaly = variance_pct >= 20 and variance >= 10

    return {
        "baseline_cost": baseline,
        "current_cost": current,
        "variance": round(variance, 2),
        "variance_pct": round(variance_pct, 2),
        "is_anomaly": is_anomaly
    }

def analyze_drivers(record):
    baseline_inv = record["baseline_invocations"]
    current_inv = record["current_invocations"]

    baseline_dur = record["baseline_duration"]
    current_dur = record["current_duration"]

    baseline_mem = record["baseline_memory"]
    current_mem = record["current_memory"]

    inv_change = ((current_inv - baseline_inv) / baseline_inv) * 100
    dur_change = ((current_dur - baseline_dur) / baseline_dur) * 100
    mem_change = ((current_mem - baseline_mem) / baseline_mem) * 100

    changes = {
        "invocations_change_pct": round(inv_change, 2),
        "duration_change_pct": round(dur_change, 2),
        "memory_change_pct": round(mem_change, 2)
    }

    driver = max(changes, key=lambda x: abs(changes[x]))

    return {
        "changes": changes,
        "primary_driver": driver
    }

def explain_with_claude(detection, analysis):
    prompt = f"""
You are a senior FinOps analyst.

Analyze the following AWS Lambda cost anomaly:

Detection:
{json.dumps(detection, indent=2)}

Driver Analysis:
{json.dumps(analysis, indent=2)}

Explain clearly:
- What caused the cost increase
- Which driver is responsible
- What it likely means technically
- What engineers should investigate

Be concise and professional.
"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text

def main():
    print("🚀 Running Lambda FinOps Agent...")

    sample_record = {
        "function_name": "payment-authorizer",
        "baseline_cost": 42.15,
        "current_cost": 89.44,
        "baseline_invocations": 100000,
        "current_invocations": 102000,
        "baseline_duration": 250,
        "current_duration": 520,
        "baseline_memory": 512,
        "current_memory": 512
    }

    detection = detect_anomaly(sample_record)

    print("\n📊 Detection Result:")
    print(json.dumps(detection, indent=2))

    if detection["is_anomaly"]:
        analysis = analyze_drivers(sample_record)

        print("\n🧠 Driver Analysis:")
        print(json.dumps(analysis, indent=2))

        explanation = explain_with_claude(detection, analysis)

        print("\n🧾 AI Explanation:")
        print(explanation)

if __name__ == "__main__":
    main()