import numpy as np

#Import Data from .CSV file
def load_grades(filename):
    #Get student information
    data = np.genfromtxt(filename, delimiter=",", dtype=str, skip_header=1)

    #Pull information for header row
    headers = np.genfromtxt(filename, delimiter=",", dtype=str, max_rows=1)

    #Extract exam names
    exams = headers[2:]

    #Grade values from str to float
    grades = data[:, 2:].astype(float)

    return headers, exams, data, grades

#Grade analysis function
def analyze_grades(headers, exams, data, grades):
    #Print sample CSV data for context
    print("Sample CSV Dataset:")
    print(headers)
    print(data[:5])

    #Perform calculations on mean, median, et al, for each exam
    print("\nExam Statistics:")
    for i in range(len(exams)):
        print(f"\n{exams[i]}:")
        print(f"Mean: {np.mean(grades[:, i]):.2f}")
        print(f"Median: {np.median(grades[:, i]):.2f}")
        print(f"Standard Deviation: {np.std(grades[:, i]):.2f}")
        print(f"Minimum: {np.min(grades[:, i]):.2f}")
        print(f"Maximum: {np.max(grades[:, i]):.2f}")

    #Print calculation results for exam totals
    print("\nOverall Statistics:")
    print(f"Mean: {np.mean(grades):.2f}")
    print(f"Median: {np.median(grades):.2f}")
    print(f"Standard Deviation: {np.std(grades):.2f}")
    print(f"Minimum: {np.min(grades):.2f}")
    print(f"Maximum: {np.max(grades):.2f}")

    #Print pass/fail %
    print("\nPass/Fail by Exam:")
    for i in range(len(exams)):
        passed = np.sum(grades[:, i] >= 60)
        failed = np.sum(grades[:, i] < 60)
        print(f"{exams[i]} - Passed: {passed}, Failed: {failed}")

    overall_pass_percentage = (np.sum(grades >= 60) / grades.size) * 100
    print(f"\nOverall Pass Percentage: {overall_pass_percentage:.2f}%")


def main():
    headers, exams, data, grades = load_grades("grades.csv")
    analyze_grades(headers, exams, data, grades)

if __name__ == "__main__":
    main()