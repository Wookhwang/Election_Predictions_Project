# SNS 동적 데이터를 바탕으로 한 여론 예측 시스템

## 개요
- 선거 전 언론사의 여론조사 결과는 실제 선거 결과에 직간접적으로 영향을 미치는 중요한 지표이다. 때문에 조사 결과에 대한 내용을 언론사들은 보다 앞다투어 보도한다. 하지만 급변하는 정보화 사회 속에 기존의 유선 방식의 여론조사는 현대사회의 실질적인 의견을 종합하지 못하는 오류를 종종 범하고 있다. SNS는 다양한 유형의 의견이나 행동들을 표출하는 하나의 수단으로 자리 잡고 있다. 다수의 언론 기관에서 이를 보다 유동적으로 조사 결과에 반영하도록 노력하고 있다. 본 프로젝트에서는 여론조사 결과와 같은 정적인 데이터가 아닌 SNS나 포털 뉴스와 같은 동적인 데이터를 활용하여 여론조사의 오차를 비교하는 시스템을 제작하는 연구를 수행하였다. 소셜미디어 데이터에선 단순히 통계자료에선 볼 수 없었던 사람들의 감정, 태도, 평가, 의견 등을 감성 분석 할 수 있을 것이라 기대된다. 이를 바탕으로 SNS의 영향력이 실제 선거 결과에 영향을 미치는지 결과를 통해 비교할 수 있을 것으로 기대한다.


## Installation
* Python 
  * version :3.6, 3.7
* Tensorflow
  * version : 2.0.0 rc
* Scikit-Learn
  * version : 0.22.1
* Download Repository and 


## 사용 방법
1. Download Repository 

2. Crawling : 원하는 플렛폼 파일을 선택한뒤 설치 경로 수정 이후에 크롤링 진행
 - Naver_Crawling은 키워드, 원하는 날짜, 최대 페이지, 관련도를 입력.
 - Youtube_Crawling은
 - Twitter_Crawling은
 
3. 1차 Data preprocessing : ~

4. 2차 Data preprocessing : Mophene의 KoNLPy_DataFrame.py을 사용하여 크롤링 파일을 DataFrame 형태로 변환

5. Regression : Regression의 Integration_Regression.py를 실행
 - 2차 Data preprocessing으로 생성한 DataFrame 파일을 Dataset으로 사용.
 - 태깅된 Data를 train, 태깅 안된 Data를 test set으로 범위를 지정해줌.
 - 이후 원하는 회귀 모델을 선택하여 예측 진행 (alpha 값은 정확도를 보고 판단)
 
6. D_Graph, M_Graph 파일을 사용하여 그래프 생성
 - D는 더불어 민주당, M은 미래통합당
 - 모델별로 확인한 예측률을 각 리스트에 입력한뒤 실행


## 라이센스
Apache 2.0


## 기여자
서동현
유제민
전현구
황욱
