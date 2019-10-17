"""
https://leetcode.com/problems/accounts-merge/

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email
that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people
as people could have the same name. A person can have any number of accounts initially, but all of their accounts
definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name,
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].

Approach:

Build graph like this

{
  "johnsmith@mail.com": {
    name: "John",
    related: [
      "john00@mail.com",
      "john_newyork@mail.com",
    ],
  },
  "john00@mail.com": {
    name: "John",
    related: [
      "johnsmith@mail.com",
    ],
  },
  "johnnybravo@mail.com": {
    name: "John",
    related: [],
  },
  "john_newyork@mail.com": {
    name: "John",
    related: [
      "johnsmith@mail.com",
    ],
  },
}

where each email encountered is the key, and each email for each person ties to the previous one.
This way, can use DFS to have entire trail of emails.
Collect all related emails for a given path, sort it, and append name.
Insert list into results.
"""


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = {}
        for account in accounts:
            name = account[0]
            email_addresses = account[1:]
            for index, email_address in enumerate(email_addresses):
                if email_address not in graph:
                    graph[email_address] = {
                        "name": name,
                        "related_email_addresses": set(),
                    }

                email_address_data = graph[email_address]
                if index > 0:
                    previous_email_address = email_addresses[index - 1]
                    previous_email_address_data = graph[previous_email_address]
                    email_address_data["related_email_addresses"].add(previous_email_address)
                    previous_email_address_data["related_email_addresses"].add(email_address)

        results = []
        visited = set()

        for email_address, data in graph.items():
            if email_address not in visited:
                combined_email_addresses = set()
                self.dfs(email_address, combined_email_addresses, graph, visited)
                results.append([data["name"]] + list(sorted(combined_email_addresses)))

        return results

    def dfs(self, email_address, combined_email_addresses, graph, visited):
        combined_email_addresses.add(email_address)
        for related_email_address in graph[email_address]["related_email_addresses"]:
            if related_email_address not in visited:
                visited.add(related_email_address)
                self.dfs(related_email_address, combined_email_addresses, graph, visited)


