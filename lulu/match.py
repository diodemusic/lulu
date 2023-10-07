import utils


def history(
    continent: str,
    puuid: str,
    queue: int,
    start: int = 0,
    count: int = 20,
) -> list:
    """Get a list of match ids by puuid.

    Args:
        continent (str): Continent str.
        puuid (str): Puuid.
        queue (int): Queue ID
        start (int, optional): Start index. Defaults to 0.
        count (int, optional): Valid values: 0 to 100. Number of match IDs to return. Defaults to 20.

    Returns:
        list: List of match IDs.
    """

    r = utils.call.make_call(
        url=f"https://{continent}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue={queue}&start={start}&count={count}"
    )

    return r


def by_match_id(continent: str, match_id: str) -> object:
    """Get a match by match id.

    Args:
        continent (str): Continent str.
        match_id (str): Match ID.

    Returns:
        object: Match object.
    """

    r = utils.call.make_call(
        url=f"https://{continent}.api.riotgames.com/lol/match/v5/matches/{match_id}"
    )

    info = r["info"]
    metadata = r["metadata"]

    participants_lst = []

    for participant in info["participants"]:
        perk_styles_lst = []

        for style in participant["perks"]["styles"]:
            style_selections_lst = []

            for selection in style["selections"]:
                style_selection = utils.classes.PerkStyleSelection(
                    perk=selection["perk"],
                    var_1=selection["var1"],
                    var_2=selection["var2"],
                    var_3=selection["var3"],
                )
                style_selections_lst.append(style_selection)

        perk_style = utils.classes.PerkStyle(
            description=style["description"],
            selections=style_selections_lst,
            style=style["style"],
        )

        perk_styles_lst.append(perk_style)

        perks = utils.classes.Perks(
            stat_perks=utils.classes.PerkStats(
                defense=participant["perks"]["statPerks"]["defense"],
                flex=participant["perks"]["statPerks"]["flex"],
                offense=participant["perks"]["statPerks"]["offense"],
            ),
            styles=perk_styles_lst,
        )

        participants_lst.append(
            utils.classes.Participant(
                assists=participant["assists"],
                baron_kills=participant["baronKills"],
                bounty_level=participant["bountyLevel"],
                champ_experience=participant["champExperience"],
                champ_level=participant["champLevel"],
                champion_id=participant["championId"],
                champion_name=participant["championName"],
                champion_transform=participant["championTransform"],
                consumables_purchased=participant["consumablesPurchased"],
                damage_dealt_to_buildings=participant["damageDealtToBuildings"],
                damage_dealt_to_objectives=participant["damageDealtToObjectives"],
                damage_dealt_to_turrets=participant["damageDealtToTurrets"],
                damage_self_mitigated=participant["damageSelfMitigated"],
                deaths=participant["deaths"],
                detector_wards_placed=participant["detectorWardsPlaced"],
                double_kills=participant["doubleKills"],
                dragon_kills=participant["dragonKills"],
                first_blood_assist=participant["firstBloodAssist"],
                first_blood_kill=participant["firstBloodKill"],
                first_tower_assist=participant["firstTowerAssist"],
                first_tower_kill=participant["firstTowerKill"],
                game_ended_in_early_surrender=participant["gameEndedInEarlySurrender"],
                game_ended_in_surrender=participant["gameEndedInSurrender"],
                gold_earned=participant["goldEarned"],
                gold_spent=participant["goldSpent"],
                individual_position=participant["individualPosition"],
                inhibitor_kills=participant["inhibitorKills"],
                inhibitor_takedowns=participant["inhibitorTakedowns"],
                inhibitors_lost=participant["inhibitorsLost"],
                item_0=participant["item0"],
                item_1=participant["item1"],
                item_2=participant["item2"],
                item_3=participant["item3"],
                item_4=participant["item4"],
                item_5=participant["item5"],
                item_6=participant["item6"],
                items_purchased=participant["itemsPurchased"],
                killing_sprees=participant["killingSprees"],
                kills=participant["kills"],
                lane=participant["lane"],
                largest_critical_strike=participant["largestCriticalStrike"],
                largest_killing_spree=participant["largestKillingSpree"],
                largest_multi_kill=participant["largestMultiKill"],
                longest_time_spent_living=participant["longestTimeSpentLiving"],
                magic_damage_dealt=participant["magicDamageDealt"],
                magic_damage_dealt_to_champions=participant[
                    "magicDamageDealtToChampions"
                ],
                magic_damage_taken=participant["magicDamageTaken"],
                neutral_minions_killed=participant["neutralMinionsKilled"],
                nexus_kills=participant["nexusKills"],
                nexus_takedowns=participant["nexusTakedowns"],
                nexus_lost=participant["nexusLost"],
                objectives_stolen=participant["objectivesStolen"],
                objectives_stolen_assists=participant["objectivesStolenAssists"],
                participant_id=participant["participantId"],
                penta_kills=participant["pentaKills"],
                perks=perks,
                physical_damage_dealt=participant["physicalDamageDealt"],
                physical_damage_dealt_to_champions=participant[
                    "physicalDamageDealtToChampions"
                ],
                physical_damage_taken=participant["physicalDamageTaken"],
                profile_icon=participant["profileIcon"],
                puuid=participant["puuid"],
                quadra_kills=participant["quadraKills"],
                riot_id_name=participant["riotIdName"],
                riot_id_tagline=participant["riotIdTagline"],
                role=participant["role"],
                sight_wards_bought_in_game=participant["sightWardsBoughtInGame"],
                spell_1_casts=participant["spell1Casts"],
                spell_2_casts=participant["spell2Casts"],
                spell_3_casts=participant["spell3Casts"],
                spell_4_casts=participant["spell4Casts"],
                summoner_1_casts=participant["summoner1Casts"],
                summoner_1_id=participant["summoner1Id"],
                summoner_2_casts=participant["summoner2Casts"],
                summoner_2_id=participant["summoner2Id"],
                summoner_id=participant["summonerId"],
                summoner_level=participant["summonerLevel"],
                summoner_name=participant["summonerName"],
                team_early_surrendered=participant["teamEarlySurrendered"],
                team_id=participant["teamId"],
                team_position=participant["teamPosition"],
                time_ccing_others=participant["timeCCingOthers"],
                time_played=participant["timePlayed"],
                total_damage_dealt=participant["totalDamageDealt"],
                total_damage_dealt_to_champions=participant[
                    "totalDamageDealtToChampions"
                ],
                total_damage_shielded_on_teammates=participant[
                    "totalDamageShieldedOnTeammates"
                ],
                total_damage_taken=participant["totalDamageTaken"],
                total_heal=participant["totalHeal"],
                total_heals_on_teammates=participant["totalHealsOnTeammates"],
                total_minions_killed=participant["totalMinionsKilled"],
                total_time_cc_dealt=participant["totalTimeCCDealt"],
                total_time_spent_dead=participant["totalTimeSpentDead"],
                total_units_healed=participant["totalUnitsHealed"],
                triple_kills=participant["tripleKills"],
                true_damage_dealt=participant["trueDamageDealt"],
                true_damage_dealt_to_champions=participant[
                    "trueDamageDealtToChampions"
                ],
                true_damage_taken=participant["trueDamageTaken"],
                turret_kills=participant["turretKills"],
                turret_takedowns=participant["turretTakedowns"],
                turrets_lost=participant["turretsLost"],
                unreal_kills=participant["unrealKills"],
                vision_score=participant["visionScore"],
                vision_wards_bought_in_game=participant["visionWardsBoughtInGame"],
                wards_killed=participant["wardsKilled"],
                wards_placed=participant["wardsPlaced"],
                win=participant["win"],
            )
        )

    teams_lst = []

    for team in info["teams"]:
        bans_lst = []

        for ban in team["bans"]:
            bans_lst.append(
                utils.classes.Ban(
                    champion_id=ban["championId"], pick_turn=ban["pickTurn"]
                )
            )

        objectives_data = team["objectives"]
        objectives_obj = utils.classes.Objectives(
            baron=utils.classes.Objective(
                first=objectives_data["baron"]["first"],
                kills=objectives_data["baron"]["kills"],
            ),
            champion=utils.classes.Objective(
                first=objectives_data["champion"]["first"],
                kills=objectives_data["champion"]["kills"],
            ),
            dragon=utils.classes.Objective(
                first=objectives_data["dragon"]["first"],
                kills=objectives_data["dragon"]["kills"],
            ),
            inhibitor=utils.classes.Objective(
                first=objectives_data["inhibitor"]["first"],
                kills=objectives_data["inhibitor"]["kills"],
            ),
            rift_herald=utils.classes.Objective(
                first=objectives_data["riftHerald"]["first"],
                kills=objectives_data["riftHerald"]["kills"],
            ),
            tower=utils.classes.Objective(
                first=objectives_data["tower"]["first"],
                kills=objectives_data["tower"]["kills"],
            ),
        )

        team_obj = utils.classes.Team(
            bans=bans_lst,
            objectives=objectives_obj,
            team_id=team["teamId"],
            win=team["win"],
        )

        teams_lst.append(team_obj)

    return utils.classes.Match(
        info=utils.classes.Info(
            game_creation=info["gameCreation"],
            game_duration=info["gameDuration"],
            game_end_timestamp=info["gameEndTimestamp"],
            game_id=info["gameId"],
            game_mode=info["gameMode"],
            game_name=info["gameName"],
            game_start_timestamp=info["gameStartTimestamp"],
            game_type=info["gameType"],
            game_version=info["gameVersion"],
            map_id=info["mapId"],
            participants=participants_lst,
            platform_id=info["platformId"],
            queue_id=info["queueId"],
            teams=teams_lst,
            tournament_code=info["tournamentCode"],
        ),
        metadata=utils.classes.Metadata(
            data_version=metadata["dataVersion"],
            match_id=metadata["matchId"],
            participants=metadata["participants"],
        ),
    )


def timeline_by_match_id(continent: str, match_id: str) -> object:
    """Get a match timeline by match id.

    Args:
        continent (str): Continent str.
        match_id (str): Match ID

    Returns:
        object: MatchTimeline object.
    """

    r = utils.call.make_call(
        url=f"https://{continent}.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline"
    )

    info = r["info"]
    metadata = r["metadata"]

    return utils.classes.MatchTimeline(
        info=utils.classes.TimelineInfo(
            frame_interval=info["frameInterval"],
            frames=info["frames"],
            game_id=info["gameId"],
            participants=info["participants"],
        ),
        metadata=utils.classes.Metadata(
            data_version=metadata["dataVersion"],
            match_id=metadata["matchId"],
            participants=metadata["participants"],
        ),
    )
