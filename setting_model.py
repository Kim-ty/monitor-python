
class SettingBuff:

    # 사냥사용
    useHunt = 1
    # 클릭주기
    clickTiming = 0.5
    # hp,mp 회복 최소값
    useHealth = 50
    # 마법사용 비트연산
    useMagic = 6
    # 보존식품
    useSaveFood = 0
    # 소환단
    useSmallHwan = 0
    # 중환단
    useMiddleHwan = 0
    # 대환단
    useBigHwan = 0
    # 태환단
    useTaeHwan = 0
    # 극환단
    useGeukHwan = 0
    # 태극단
    useTaegeukHwan = 0
    # 네모송편
    useSquireDuck = 0
    # 무지개떡
    useRainbowDcuk = 0
    # 기운석
    useEnergyStone = 0
    # 경치배율템
    useExp = 0
    # 군주정신력
    useGoonzuMentality = 0
    # 천지환
    useWorldHwan = 0
    # 편지
    useLetter = 0

    def __init__(self,buff_list):
        for key,value in buff_list.items():
            exec('%s = %s' % (key,value))