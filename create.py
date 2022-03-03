import subprocess


def main():
    question_head = "ABCDEFGHIJKLMNOP"
    is_atcoder_contest = ""

    while is_atcoder_contest != "y" and is_atcoder_contest != "n":
        is_atcoder_contest = input("[?] ABC/ARC/AGC [y/n] : ")

    if is_atcoder_contest == "n":
        contest_yyyymmdd = ""
        contest_name = ""
        n_question = ""

        while len(contest_yyyymmdd) != 8 or not contest_yyyymmdd.isdigit():
            contest_yyyymmdd = input("[?] Contest date (yyyymmdd) : ")

        while contest_name == "":
            contest_name = input("[?] Contest name : ")

        while not n_question.isdigit():
            n_question = input("[?] Number of questions : ")
        n_question = int(n_question)

        directory_name = "./Others/{}_{}".format(contest_yyyymmdd, contest_name)
        subprocess.call(["mkdir", directory_name])

        for question_i in range(n_question):
            directory_file_name = directory_name + "/{}.py".format(
                question_head[question_i]
            )

            subprocess.call(["cp", "./Template.py", directory_file_name])

    else:
        contest_name = ""
        contest_number = ""
        n_question = ""

        while contest_name not in ["ABC", "ARC", "AGC"]:
            contest_name = input("[?] Contest name (ABC/ARC/AGC) : ")

        while not contest_number.isdigit():
            contest_number = input("[?] Contest number : ")
        contest_number = int(contest_number)

        while not n_question.isdigit():
            n_question = input("[?] Number of questions : ")
        n_question = int(n_question)

        if contest_name == "ABC":
            directory_name = "./AtCoder_Beginner_Contest/{:03d}".format(contest_number)
        elif contest_name == "ARC":
            directory_name = "./AtCoder_Regular_Contest/{:03d}".format(contest_number)
        elif contest_name == "AGC":
            directory_name = "./AtCoder_Grand_Contest/{:03d}".format(contest_number)

        subprocess.call(["mkdir", directory_name])

        for question_i in range(n_question):
            directory_file_name = directory_name + "/{}.py".format(
                question_head[question_i]
            )

            subprocess.call(["cp", "./Template.py", directory_file_name])


if __name__ == "__main__":
    main()
