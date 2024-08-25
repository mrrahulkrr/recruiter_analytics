from flask import Blueprint, request, jsonify
from app.models import RecruitmentData
from app.predictive_analytics import PredictiveAnalytics
from app.trend_analysis import TrendAnalysis
from app import db

bp = Blueprint('main', __name__)

pa = PredictiveAnalytics()
ta = None

@bp.before_app_request
def initialize_models():
    global ta
    data = RecruitmentData.query.all()
    df = pd.DataFrame([d.to_dict() for d in data])
    pa.train_models(df)
    ta = TrendAnalysis(df)

@bp.route('/predict/time_to_hire', methods=['POST'])
def predict_time_to_hire():
    features = request.json
    prediction = pa.predict_time_to_hire(features)
    return jsonify({'prediction': prediction})

@bp.route('/predict/candidate_success', methods=['POST'])
def predict_candidate_success():
    features = request.json
    prediction = pa.predict_candidate_success(features)
    return jsonify({'prediction': prediction})

@bp.route('/trend/analyze', methods=['POST'])
def analyze_trend():
    params = request.json
    trend_data = ta.analyze_trend(params['metric'], params['time_period'])
    return jsonify(trend_data)

@bp.route('/trend/plot', methods=['POST'])
def plot_trend():
    params = request.json
    plot_data = ta.plot_trend(params['metric'], params['time_period'])
    return jsonify({'plot': plot_data})

@bp.route('/trend/compare', methods=['POST'])
def compare_trends():
    params = request.json
    plot_data = ta.compare_trends(params['metric1'], params['metric2'], params['time_period'])
    return jsonify({'plot': plot_data})