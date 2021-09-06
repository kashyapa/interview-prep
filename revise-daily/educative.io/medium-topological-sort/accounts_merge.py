def accountsMerge(accounts):
    def find(a):
        if ds[a] < 0:
            return a
        ds[a] = find(ds[a])
        return ds[a]

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            if ds[a] < ds[b]:
                ds[a] += ds[b]
                ds[b] = a
            else:
                ds[b] += ds[a]
                ds[a] = b

    c, ds, email_to_id, id_to_name = 0, [], {}, {}
    for account in accounts:
        for email in account[1:]:
            if email not in email_to_id:
                email_to_id[email] = c
                id_to_name[c] = account[0]
                ds.append(-1)
                c += 1
            union(email_to_id[account[1]], email_to_id[email])

    res = {}
    for email, id in email_to_id.items():
        master = find(id)
        res[master] = res.get(master, []) + [email]
    return [[id_to_name[id]] + sorted(emails) for id, emails in res.items()]


if __name__ == "__main__":
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]

    print(accountsMerge(accounts))
