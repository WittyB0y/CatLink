SQL_QUERY = '''WITH LinkCount AS (
SELECT user_id, COUNT(*) AS count_links, COUNT(CASE WHEN link_type = 1 THEN 1 END) AS website,
COUNT(CASE WHEN link_type = 2 THEN 1 END) AS book,
        COUNT(CASE WHEN link_type = 3 THEN 1 END) AS article,
        COUNT(CASE WHEN link_type = 4 THEN 1 END) AS music,
        COUNT(CASE WHEN link_type = 5 THEN 1 END) AS video
    FROM Link_link
    GROUP BY user_id
),
MaxLinkCount AS (
    SELECT MAX(count_links) AS max_count
    FROM LinkCount
),
MaxUsers AS (
    SELECT user_id
    FROM LinkCount
    WHERE count_links = (SELECT max_count FROM MaxLinkCount)
),
OldestUser AS (
    SELECT user_id
    FROM auth_user
    WHERE id IN (SELECT user_id FROM MaxUsers)
    ORDER BY date_joined ASC
    LIMIT 10
)
SELECT auth_user.email,
LinkCount.count_links AS count_links,
    LinkCount.website,
    LinkCount.book,
    LinkCount.article,
    LinkCount.music,
    LinkCount.video
FROM auth_user
LEFT JOIN LinkCount ON auth_user.id = LinkCount.user_id
WHERE auth_user.id IN (SELECT user_id FROM OldestUser)
ORDER BY LinkCount.count_links DESC, auth_user.date_joined ASC
LIMIT 10;
'''
