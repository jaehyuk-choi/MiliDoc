# raw_text = input("문장을 입력해주세요: ")
raw_text = """군과 민간이 공동으로 이용할 대구 통합신공항을 대구에서 경북 군위로 이전해 건설하는 내용의 청사진이 마련됐다.

국방부는 18일 대구시와 함께 대구 군 공항 이전 사업 관련 ‘대구 통합신공항 기본계획’ 수립을 완료했다고 밝혔다.

이번 기본계획은 대구시 주관으로 국방부, 공군 등과 함께 지난 2020년 11월 계획 수립을 위한 용역을 발주한 지 1년 9개월만이다.

이 계획 안에는 활주로 위치와 방향, 주요 군부대 시설 규모 및 배치계획, 총사업비 등의 내용이 포함돼 있다.

국방부는 그동안 대구시와 함께 대구 군 공항에 대한 현장실사 및 공군, 미7공군, 국토부, 외교부 등 관계 기관과 “긴밀한 협의를 통해 기본계획을 수립했다”고 설명했다.

특히 공군과 협의를 통해 군사작전 적합성을 검토하고, 소음 피해를 최소화하는 최적의 활주로 위치와 방향을 결정했다고 전했다.

국방부는 현 기지 사용부대, 관계 기관과 50여 차례 협의를 통해 현장실사를 거쳐 한국군부대 시설 규모 및 배치 계획을 수립했고, 주한미군, 미 7공군 등과 30여 차례의 실무 협의를 통해 미군 시설 이전 소요를 기본계획에 반영했다.

이에 따라 국방부는 대구시와 합의각서(안)을 작성, 이달 말쯤 기획재정부에 ‘기부 대 양여’ 심의(안)을 제출할 예정이다.

국방부는 또 미 국무부가 지난 7월 중순 주한미군사령부로 협상 권한 위임 절차를 마쳐 “미군시설 이전의 기본 원칙과 절차를 정하는 포괄협정 협상 등도 차질없이 진행할 계획”이라고 밝혔다.

한편 대구경북 통합신공항 이전 후보지인 경북 군위군이 속해 있는 경북도는 이날 공항 이전 지역을 개발행위 허가 제한지역으로 지정하는 논의에 착수하는 등 후속 조치에 들어갔다.

대구 통합신공항 후보지가 개발행위허가 제한지역으로 지정되면 ‘국토의 계획 및 이용에 관한 법률’에 따라 건축물의 건축 또는 공작물의 설치, 토지의 형질 변경 등이 제한된다. 이는 대규모 개발 사업에 따른 투기성 건축행위를 막기 위한 것이다.

오는 9월 7일 대구 통합신공항 범도민추진위원회도 출범할 예정이다.

출처 : 국방신문(http://www.gukbangnews.com)
# """
raw_text = ''' 국방혁신 4.0을 통한 첨단과학기술軍 육성’ 측면에서,
   ◦AI 기술 수준과 발전단계를 고려하여 국방AI 발전모델’을 정립하였으며, 이에 따라 우리 軍에 대한 AI 기술 적용을 단계적으로 확대해 나갈 것입니다.
     ∙먼저, 1단계는 ‘초기자율형’으로 AI 기반의 다출처 영상융합체계, GOP･해안경계체계를 발전시키고,
     ∙2단계는 ‘반자율형’으로 무인 전투차량, 수상정 등 ‘유･무인 복합 전투체계’등에 AI 기술을 접목하며,
     ∙3단계는 ‘완전 자율형’으로 ‘지능형 지휘결심지원체계’,  ‘초연결 전투체계’ 등이 구현될 수 있도록 추진하겠습니다.
 kk  q'''

from konlpy.tag import Mecab
tokenizer = Mecab()

raw_text_morphs = tokenizer.morphs(raw_text)
print(raw_text_morphs)