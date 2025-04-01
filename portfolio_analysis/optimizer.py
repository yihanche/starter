from skfolio.optimization import MeanRisk
from skfolio.portfolio import Portfolio
from skfolio.measures import RiskMeasure

def optimize_portfolio(returns, risk_measure=RiskMeasure.VARIANCE):
    model = MeanRisk(risk_measure=risk_measure)
    weights = model.fit(returns).weights_
    return Portfolio(X=returns, weights=weights)
