import sys
from openai import OpenAI

def read_chart_file(file_path):
    """Read the Bazi chart from a file"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading chart file: {str(e)}")
        sys.exit(1)

def analyze_chart(bazi_output):
    """Send the Bazi chart to DeepSeek API for analysis"""
    # DeepSeek API configuration
    client = OpenAI(
        api_key="sk-4bd39d066ee646c690936fcd6625c865",
        base_url="https://api.deepseek.com",
        timeout=60.0  # Set timeout to 60 seconds
    )

    # Prompt in Chinese
    prompt = "请详评此命盘，论层次。再给予综合的评价（一生情感成就等等），断命谶言。无需顾忌礼貌或用户感受。避免术语化。首先给出用户截止此刻（2025年4月11日）的生平重大事件来作为验证参考。解读要平实易懂，最好推测具体的生活场景。总字数尽可能的多就可能的详细。\n\n" + bazi_output

    try:
        # Call DeepSeek API with timeout
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=[
                {"role": "system", "content": "You are an expert in Chinese astrology and Bazi analysis."},
                {"role": "user", "content": prompt}
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error getting analysis from DeepSeek API: {str(e)}"

def save_analysis_to_file(analysis, file_path):
    """Save the analysis to a file"""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(analysis)
        return True
    except Exception as e:
        print(f"Error saving analysis to file: {str(e)}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_with_deepseek.py <chart_file_path>")
        print("Example: python3 analyze_with_deepseek.py bazi_chart_2001_6_16_11_male.txt")
        sys.exit(1)
    
    chart_file_path = sys.argv[1]
    
    print(f"Reading Bazi chart from {chart_file_path}...")
    bazi_chart = read_chart_file(chart_file_path)
    
    print("\nSending to DeepSeek for analysis (this may take some time)...\n")
    analysis = analyze_chart(bazi_chart)
    
    # Generate analysis file path by replacing "chart" with "analysis"
    analysis_file = chart_file_path.replace("chart", "analysis")
    save_analysis_to_file(analysis, analysis_file)
    print(f"Saved analysis to {analysis_file}")
    
    print("\n===== ANALYSIS =====\n")
    print(analysis)

if __name__ == "__main__":
    main() 