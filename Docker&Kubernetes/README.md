# 🎤 1차 기술세미나 발표 요약: EFSVM과 불균형 데이터셋

---

## 📌 발표 주제
- **데이터 불균형 문제 해결을 위한 Entropy 기반 Fuzzy SVM**
- 본 프로젝트는 불균형 데이터셋 문제를 해결하기 위한 **Entropy 기반 Fuzzy SVM (EFSVM)**을 구현하고 성능을 비교·분석한 연구입니다.  

---

## 🎯 Why 이 주제인가?
- 금융 도메인에서는 **정확도(Accuracy)** 보다 **소수 클래스에 대한 F-1 Score** 이 더 중요  
- 소수 클래스(사기 거래) 탐지를 놓치면 실제 피해 발생  
- 기존 ML/DL 모델은 다수 클래스에 치우쳐 있음 → 해결책 필요  

---

## 🔍 불균형 데이터셋이란?
- 클래스 간 데이터 비율이 크게 차이 나는 경우  
- 예시: 정상거래 99.8% vs 사기거래 0.2%  
- 문제점: Accuracy는 높아도 소수 클래스(양성) 검출 실패  

---

## ⚙️ EFSVM 개념
- **Fuzzy SVM**: 샘플별 중요도 가중치 부여 → 노이즈 완화  
- **Entropy 추가**: 불확실성을 정량화 → 소수 클래스 비중 강화  

---

## 🧪 실험 요약
- **데이터셋**: Fraudulent Transaction Detection ([Kaggle](https://www.kaggle.com/datasets/sanskar457/fraud-transaction-detection))   
양성:음성 비율 약 86.5:13.5
- **비교 모델**: EFSVM(제안 모델), SVM, Logistic Regression, Random Forest, XGBoost  
모든 모델은 동일한 전처리 및 컬럼 선택 적용  
주요 하이퍼파라미터는 라이브러리의 기본 값으로 설정
- **성능 평가**:F1-score  
클래스별 산출 (양성Neg/음성)  

| Model                  | F1-score(Negative)      | F1-score(Positive)   |
|------------------------|-------------------------|----------------------|
| logstic regression     |       0.8576            |   0.5476             |
| RandomForest           | 0.9858                  |       0.8983         |
| XGBoost                | 0.9963                  |       0.9755         |
| SVM                    | 0.9058                  |       0.6358         |
| **EFSVM**              | 0.9926                  | **0.9559**           |



---

## 📊 시각자료
<img width="1023" height="562" alt="Image" src="./img/f1_score_barplot.png"/>
---

## 📝 결론
- 현재 EFSVM은 기존 머신러닝 모델 대비 분류 성능에서 다소 한계가 있음  
- 그러나 IEFSVM과 같은 새로운 변형 모델이 지속적으로 제안되며 진화 중  
-> 향후 더 높은 설명가능성과 우수한 분류 성능을 동시에 갖춘 모델로 발전할 것으로 기대됨

---

## 📚 참고자료
조풍진, "Instance-based Entropy Classifier for Imbalanced Classification Problem", 서울대학교 박사학위논문
Chun-Fu Lin, Sheng-De Wang"Fuzzy Support Vector Machines"
https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing?utm_source=chatgpt.com https://arxiv.org/abs/1902.11097?utm_source=chatgpt.com https://pmc.ncbi.nlm.nih.gov/articles/PMC9374341/?utm_source=chatgpt.com https://www.statnews.com/2021/06/21/epic-sepsis-prediction-tool/?utm_source=chatgpt.com
https://gsis.kwdi.re.kr/statHtml/statHtml.do?orgId=338&tblId=DT_1XI2040 https://kosis.kr/statHtml/statHtml.do?sso=ok&returnurl=https%3A%2F%2Fkosis.kr%3A443%2FstatHtml%2FstatHtml.do%3FtblId%3DDT_1BPA002%26orgId%3D101%26checkFlag%3DN%26
https://www.ibm.com/kr-ko/think/topics/support-vector-machine
https://news.samsungdisplay.com/24757
https://wikidocs.net/257250
https://www.youtube.com/watch?v=__0nZuG4sTw&t=658s
https://aiflower.tistory.com/5
