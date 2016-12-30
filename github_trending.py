import datetime

import requests


def get_trending_repositories(quantity=20):
    date_7_days_ago = datetime.date.today() - datetime.timedelta(days=7)
    payload = {
        'q': 'created:>{}'.format(date_7_days_ago),
        'sort': 'stars',
        'per_page': quantity,
        }
    repositories_url = 'https://api.github.com/search/repositories'
    trending_repositories = requests.get(repositories_url, params=payload)
    return trending_repositories.json()['items']


def get_printable_repository_info(repository):
    title = repository['full_name']
    stars = repository['stargazers_count']
    open_issues = repository['open_issues_count']
    url = repository['html_url']
    printable_info = ('{stars} star(s), project: {title}, open issues: '
                      '{open_issues}, url: {url}'.format(
                          stars=stars,
                          title=title,
                          open_issues=open_issues,
                          url=url,
                          ))
    return printable_info


if __name__ == '__main__':
    trending_repositories = get_trending_repositories()
    print('Last 7 days trending projects on GitHub:', end='\n\n')
    for repository in trending_repositories:
        print(get_printable_repository_info(repository))
