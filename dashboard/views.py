# dashboard/views.py

from django.shortcuts import render, redirect
from .forms import AddGameDataForm
from router.agent_pipeline import run_agent_pipeline
import pandas as pd
import os
import json

def dashboard_home(request):
    csv_path = os.path.join("data", "team_x_games.csv")
    
    context = {
        "add_data_form": AddGameDataForm(),
        "analysis_report": request.session.get('analysis_report'),
        "sw_report": request.session.get('sw_report'),
        "strategy_report": request.session.get('strategy_report'),
        "csv_data": None,
        "scroll_to_id": request.session.pop('scroll_to_id', None),
        "chart_data": request.session.get('chart_data')
    }

    if request.method == "POST":
        if 'clear_reports' in request.POST:
            request.session.flush()
            return redirect('dashboard_home')

        query = ""
        report_type = None
        scroll_target = None

        if 'analyze_general' in request.POST:
            query = "Analyze the last 20 games from the provided data. Provide a comprehensive summary of team performance, noting any trends."
            report_type = 'analysis_report'
            scroll_target = 'report-analysis'
            
            try:
                df = pd.read_csv(csv_path)
                required_cols = ['game_result', 'total_fast_breaks', '3pt_defense_failures', '3pt_success_by_opponent']
                if not df.empty and all(col in df.columns for col in required_cols):
                    performance_summary = df.groupby('game_result')[required_cols[1:]].mean().reset_index()
                    chart_labels = ['Total Fast Breaks', '3pt Defense Failures', 'Opponent 3pt Success']
                    win_data, loss_data = [0, 0, 0], [0, 0, 0]

                    win_row = performance_summary[performance_summary['game_result'] == 'win']
                    if not win_row.empty: win_data = win_row.iloc[0, 1:].values.tolist()

                    loss_row = performance_summary[performance_summary['game_result'] == 'loss']
                    if not loss_row.empty: loss_data = loss_row.iloc[0, 1:].values.tolist()
                    
                    if any(v > 0 for v in win_data) or any(v > 0 for v in loss_data):
                        request.session['chart_data'] = json.dumps({
                            "labels": chart_labels,
                            "winData": win_data,
                            "lossData": loss_data
                        })
            except Exception as e:
                print(f"Error generating chart data: {e}")

        elif 'analyze_strengths_weaknesses' in request.POST:
            query = "Focus specifically on identifying the opponent's core strengths..."
            report_type = 'sw_report'
            scroll_target = 'report-sw'

        elif 'build_strategy' in request.POST:
            query = "Acting as a world-class basketball strategist, develop a comprehensive game plan..."
            report_type = 'strategy_report'
            scroll_target = 'report-strategy'

        elif 'add_data' in request.POST:
            add_form = AddGameDataForm(request.POST)
            if add_form.is_valid():
                # Create a DataFrame from the form's cleaned data
                new_row = pd.DataFrame([add_form.cleaned_data])

                # --- NEW: Rename columns to match the CSV file ---
                column_mapping = {
                    'three_pt_defense_failures': '3pt_defense_failures',
                    'three_pt_success_by_opponent': '3pt_success_by_opponent'
                }
                new_row.rename(columns=column_mapping, inplace=True)
                # ----------------------------------------------------

                new_row.to_csv(csv_path, mode='a', header=not os.path.exists(csv_path), index=False)
                return redirect('dashboard_home')
        
        if query and report_type:
            agent_output = run_agent_pipeline(query, csv_path)
            request.session[report_type] = agent_output
            request.session['scroll_to_id'] = scroll_target
            return redirect('dashboard_home')

    try:
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            context['csv_data'] = df.to_dict("records")
    except Exception as e:
        print(f"Error reading CSV for table: {e}")

    return render(request, 'home.html', context)