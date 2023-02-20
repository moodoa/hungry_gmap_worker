import requests
from bs4 import BeautifulSoup


class JOB:
    def __init__(self, keyword, city):
        city_codes = {
            "台北市": "6001001000",
            "新北市": "6001002000",
            "桃園市": "6001003000",
            "台中市": "6001004000",
            "台南市": "6001005000",
            "高雄市": "6001006000",
            "宜蘭縣": "6001007000",
            "新竹市": "6001008000",
            "新竹縣": "6001008000",
            "苗栗縣": "6001010000",
            "彰化縣": "6001011000",
            "南投縣": "6001012000",
            "雲林縣": "6001013000",
            "嘉義縣": "6001014000",
            "嘉義市": "6001014000",
            "屏東縣": "6001016000",
            "台東縣": "6001017000",
            "花蓮縣": "6001018000",
            "金門縣": "6001020000",
            "澎湖縣": "6001021000",
            "基隆市": "6001009000",
            "新竹市": "6001019000",
            "嘉義市": "6001020000",
            "連江縣": "6001022000",
            "全部地區": "6001000000",
        }
        self.keyword = keyword
        self.city_code = city_codes[city]

    def hunting(self, page):
        url = "https://www.104.com.tw/jobs/search/"
        params = {
            "keyword": self.keyword,
            "area": self.city_code,
            "order": "1",
            "asc": "1",
            "page": page,
            "mode": "s",
        }
        response = requests.get(url, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("article", {"class": "js-job-item"})
        return jobs

    def collect_jobs(self, cnt):
        page = 1
        jobs_infos = []
        while len(jobs_infos) < cnt:
            jobs = self.hunting(page)
            if not jobs:
                break
            jobs_infos += self.parse_soup(jobs)
            page += 1
            if len(jobs_infos) >= cnt:
                break
        return sorted(jobs_infos[:cnt], key=lambda x: x["job_date"], reverse=True)

    def parse_soup(self, jobs):
        jobs_infos = []
        for job in jobs:
            jobs_info = {}
            try:
                if job.find("span", {"class": "b-tit__date"}).text.strip() != "":
                    jobs_info["job_title"] = job.find(
                        "a", {"class": "js-job-link"}
                    ).text
                    jobs_info["job_link"] = job.find("a", {"class": "js-job-link"})[
                        "href"
                    ][2:]
                    jobs_info["job_company"] = job["data-cust-name"]
                    jobs_info["job_location"] = (
                        job.find("ul", {"class": "job-list-intro"})
                        .find_all("li")[0]
                        .text
                    )
                    jobs_info["job_salary"] = job.find(
                        "span", {"class": "b-tag--default"}
                    ).text
                    jobs_info["job_date"] = job.find(
                        "span", {"class": "b-tit__date"}
                    ).text.strip()
                    jobs_infos.append(jobs_info)
            except:
                pass
        return jobs_infos

    def make_output(self, jobs_infos):
        output = ""
        for jobs_info in jobs_infos:
            output += "🪓\n"
            output += f"{jobs_info['job_title']}\n\n"
            output += f"{jobs_info['job_company']}\n\n"
            output += f"{jobs_info['job_location']}\n\n"
            output += f"{jobs_info['job_salary']}\n\n"
            output += f"更新日期: {jobs_info['job_date']}\n\n"
            output += f"{jobs_info['job_link']}\n\n\n"
        return output