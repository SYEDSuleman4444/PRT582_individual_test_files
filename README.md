# PRT582 Online Movie Booking System — Testing Artefacts

Student: Syed Suleman Uddin Farhad Syed (S403360)  
Group: Sydney Group 1  
Project: Online Movie Booking System

This folder contains testing artefacts to commit alongside the project or in a separate testing repository.



## Contents
- `robot/functional_tests.robot` — starter browser-based functional tests using Robot Framework and SeleniumLibrary.
- `locust/locustfile.py` — Locust load-test scenario for the local application.
- `security/security_review.md` — safe manual security checklist and result template.
- `manual/functional_test_cases.md` — manual acceptance cases and recording template.
- `evidence/README.md` — what genuine screenshots and reports to add.
- `requirements-test.txt` — Python testing dependencies.

## 1. Prerequisites
Use a supported Python version compatible with the selected test tools. The legacy application itself may require an older Python/Django stack; run it in the environment specified by its own README. Do not change the app's dependencies merely to make the test tools install.

Install test tools in a separate environment:
```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-test.txt
```

Install a compatible Chrome browser and ChromeDriver, or configure Selenium Manager if your installed Selenium version supports it.

## 2. Start the application
Follow the application's original README. For the current local setup, the test scripts default to:
`http://127.0.0.1:8000`

Change `BASE_URL` / Locust host only if your application uses another local URL. Do not run load/security checks against a website you do not own or have permission to test.

## 3. Run Robot Framework tests
From this folder:
```bash
robot --outputdir results/robot robot/functional_tests.robot
```
The output directory contains `report.html`, `log.html`, and `output.xml` after execution. Commit a short report or selected logs if required by your unit, but do not commit personal data, credentials, cookies, or secrets.

If a test fails because a locator does not match the application's actual HTML, inspect the page and update the locator. Do not label an unexecuted or blocked test as passed.

## 4. Run Locust
Start the application first, then:
```bash
locust -f locust/locustfile.py --host http://127.0.0.1:8000
```
Open the local Locust interface shown in the terminal and select a small number of users for a short test first. Use a low load on a local development server. To save headless CSV/HTML evidence:
```bash
locust -f locust/locustfile.py --host http://127.0.0.1:8000 --headless -u 1 -r 1 -t 30s --csv results/locust/smoke --html results/locust/report.html
```
Create `results/locust` first. Do not start with 100 users; validate the scenario with 1–5 users and increase gradually.

## 5. Security checks
Use `security/security_review.md` as a checklist. Bandit can review Python source code:
```bash
python -m pip install bandit
bandit -r ../ -f txt -o results/bandit.txt
```
Run it from a suitable project folder and exclude virtual environments/build artefacts. Review every finding manually.

## 6. Evidence to commit
See `evidence/README.md`. Include genuine screenshots from your own execution, plus concise test logs/reports. Do not commit `.venv`, passwords, database credentials, `SECRET_KEY`, cookies, or large unfiltered logs.

## 7. GitHub push
If you are adding this to an existing cloned repository:
```bash
git status
git add README.md requirements-test.txt robot locust security manual evidence
git commit -m "Add PRT582 testing artefacts"
git push
```
If the repository is not cloned, use GitHub's **Add file → Upload files** for a small set, or clone the repository and use Git commands. Never overwrite other group members' work without coordinating first.
