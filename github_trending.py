import datetime

import requests


NUMBER_OF_DAYS_TO_FETCH = 7


def get_trending_repositories(repositories_quantity=20):
    date_n_days_ago = datetime.date.today() - datetime.timedelta(
        days=NUMBER_OF_DAYS_TO_FETCH)
    payload = {
        'q': 'created:>{}'.format(date_n_days_ago),
        'sort': 'stars',
        'per_page': repositories_quantity,
        }
    repositories_url = 'https://api.github.com/search/repositories'
    trending_repositories = requests.get(repositories_url, params=payload)
    return trending_repositories.json()['items']


def get_printable_repository_info(repository):
    printable_info = ('{stars} star(s), project: {title}, open issues: '
                      '{open_issues}, url: {url}'.format(
                          stars=repository['stargazers_count'],
                          title=repository['full_name'],
                          open_issues=repository['open_issues_count'],
                          url=repository['html_url'],
                          ))
    return printable_info


if __name__ == '__main__':
    trending_repositories = get_trending_repositories()
    print('Last {} days trending projects on GitHub:'.format(
        NUMBER_OF_DAYS_TO_FETCH), end='\n\n')
    for repository in trending_repositories:
        print(get_printable_repository_info(repository))
