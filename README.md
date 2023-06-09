# Proceedings Scrapers
These are a collection of scrapers to automatically extract a list of paper titles and relevant information from the proceedings of selected academic conferences.

These scrapers are originally written for `STMETHD` class of De La Salle University.

## Current Scraper List

1. [AAAI '22](https://aaai.org/proceeding/aaai-36-2022/): scrapes all paper titles and authors from the technical sessions.
2. [IJCAI '22](https://www.ijcai.org/proceedings/2022/): scrapes all paper titles and authors from the main conference.
3. [ICML '22](https://proceedings.mlr.press/v162/): scrapes all paper titles and authors from the main conference.
4. [NeurIPS '22 Main Conference](https://papers.nips.cc/paper_files/paper/2022): scrapes all paper titles and authors from the main conference.
5. [NeurIPS '22 Datasets and Benchmarks Track](https://papers.nips.cc/paper_files/paper/2022): scrapes all paper titles and authors from the datasets and benchmarks track.
6. [ICLR '22](https://openreview.net/group?id=ICLR.cc/2022/Conference): scrapes all paper titles and authors from the main conference.
7. [ACL '22](https://aclanthology.org/events/acl-2022/#2022acl-long): scrapes all paper titles, links, and authors from the main conference (long papers only).
8. [EMNLP '22](https://aclanthology.org/events/emnlp-2022/#2022emnlp-main): scrapes all paper titles, links, and authors from the main conference.
9. [NAACL '22](https://aclanthology.org/events/naacl-2022/#2022naacl-main): scrapes all paper titles, links, and authors from the main conference.
10. [AIED '22](https://link.springer.com/book/10.1007/978-3-031-11644-5): scrapes all paper titles, links, and authors of full papers from the main conference (Note: AIED does not provide free full paper access, so the links only point to the paper page in the proceedings).

## Usage
Use `pipenv install` to install requirements.

Run the individual scraper files in the `./scraper` directory. The results will be dumped as a `.json` file in under the `./results` folder.