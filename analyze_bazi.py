import subprocess
import sys
import time

def generate_bazi_chart(year, month, day, hour, gender="male"):
    """Generate a Bazi chart using the bazi.py script"""
    try:
        # Add -n flag for female gender
        if gender.lower() == "female":
            cmd = ["python3", "bazi.py", "-g", "-n", str(year), str(month), str(day), str(hour)]
        else:
            cmd = ["python3", "bazi.py", "-g", str(year), str(month), str(day), str(hour)]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running bazi.py: {result.stderr}")
            sys.exit(1)
        return result.stdout
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def save_chart_to_file(chart, file_path):
    """Save the Bazi chart to a file"""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(chart)
        return True
    except Exception as e:
        print(f"Error saving chart to file: {str(e)}")
        return False

def main():
    if len(sys.argv) < 5:
        print("Usage: python3 analyze_bazi.py <year> <month> <day> <hour> [gender]")
        print("Example: python3 analyze_bazi.py 2001 6 16 11 male")
        print("Example: python3 analyze_bazi.py 2001 6 16 11 female")
        sys.exit(1)
    
    year = sys.argv[1]
    month = sys.argv[2]
    day = sys.argv[3]
    hour = sys.argv[4]
    
    # Optional gender parameter, defaults to male
    gender = "male"
    if len(sys.argv) >= 6:
        gender = sys.argv[5]
    
    print(f"Generating Bazi chart for {gender} with birth date: {year}-{month}-{day} {hour}:00...")
    bazi_chart = generate_bazi_chart(year, month, day, hour, gender)
    
    # Save the chart to a file
    chart_file = f"bazi_chart_{year}_{month}_{day}_{hour}_{gender}.txt"
    save_chart_to_file(bazi_chart, chart_file)
    print(f"Saved chart to {chart_file}")
    
    print("\n===== BAZI CHART =====\n")
    print(bazi_chart)
    
    print("\nTo get an analysis, run the following command manually:")
    print(f"python3 analyze_with_deepseek.py {chart_file}")

if __name__ == "__main__":
    main() 