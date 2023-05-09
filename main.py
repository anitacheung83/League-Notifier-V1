import discord_bot

if __name__ == '__main__':
    discord_bot.run_discord_bot()
# import riot_requests
# import responses
# from weekly_report import WeeklyReport

# weekly_report = responses.weekly_report("sosadtobad")

# print(weekly_report.matches_by_date)

# import matplotlib.pyplot as plt

# summoner = riot_requests.get_summoners_by_name("kid orpheus")


# matches = riot_requests.get_matches_by_puuid(summoner.puuid)

# past_match = riot_requests.get_matches_by_match_id("NA1_4620414214")

# print(past_match.start_time)
# print(past_match.end_time)
# print(past_match.duration)
# print(past_match.teams)

# for team in past_match.teams:
#     print(team.win)
#     print(team.participants)


# print(summoner)

# matches = riot_requests.get_last_week_matches_by_puuid(summoner.puuid)

# matches0 = []

# for i in range(len(matches)):
#     # print(f"Match {i}")
#     match = riot_requests.get_matches_by_match_id(matches[i])
#     matches0.append(match)

# weekly_report = WeeklyReport(summoner, matches0)

# print(weekly_report.matches_by_date.keys())

# f = weekly_report.graph

# plt.show()

# matches0 = riot_requests.get_matches_by_puuid(summoner.puuid)

# for i in range(len(matches0)):
#     print(f"Match {i}")
#     match = riot_requests.get_matches_by_match_id(matches0[i])
#     print(match)


# match = riot_requests.get_matches_by_match_id(matches[0])

# print(match)
