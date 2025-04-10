import subprocess
import sys
from openai import OpenAI

def generate_bazi_chart(year, month, day, hour):
    """Generate a Bazi chart using the bazi.py script"""
    try:
        cmd = ["python3", "bazi.py", "-g", str(year), str(month), str(day), str(hour)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running bazi.py: {result.stderr}")
            sys.exit(1)
        return result.stdout
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def analyze_chart(bazi_output):
    """Send the Bazi chart to DeepSeek API for analysis"""
    # DeepSeek API configuration
    client = OpenAI(
        api_key="sk-4bd39d066ee646c690936fcd6625c865",
        base_url="https://api.deepseek.com"
    )

    # Prompt in Chinese
    prompt = "请详评此命盘，给予综合的评价（一生情感成就等等），断命谶言。\n\n" + bazi_output

    # Call DeepSeek API
    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[
            {"role": "system", "content": "You are an expert in Chinese astrology and Bazi analysis."},
            {"role": "user", "content": prompt}
        ],
        stream=False
    )

    return response.choices[0].message.content

def main():
    if len(sys.argv) < 5:
        print("Usage: python3 analyze_bazi.py <year> <month> <day> <hour>")
        print("Example: python3 analyze_bazi.py 2001 6 16 11")
        sys.exit(1)
    
    year = sys.argv[1]
    month = sys.argv[2]
    day = sys.argv[3]
    hour = sys.argv[4]
    
    print(f"Generating Bazi chart for birth date: {year}-{month}-{day} {hour}:00...")
    bazi_chart = generate_bazi_chart(year, month, day, hour)
    
    print("\nSending to DeepSeek for analysis...\n")
    analysis = analyze_chart(bazi_chart)
    
    print("\n===== ANALYSIS =====\n")
    print(analysis)

if __name__ == "__main__":
    main() 