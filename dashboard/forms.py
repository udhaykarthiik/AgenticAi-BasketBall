# dashboard/forms.py

from django import forms

class AddGameDataForm(forms.Form):
    # Note: We'll skip game_id and let the CSV handle it or auto-increment later.
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', "class": "form-control"})
    )
    opponent = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    play_type = forms.ChoiceField(
        choices=[('fast_break', 'Fast Break'), ('halfcourt', 'Half-court')], 
        widget=forms.Select(attrs={"class": "form-control"})
    )
    initiated_by = forms.ChoiceField(
        choices=[('PG', 'Point Guard'), ('SG', 'Shooting Guard'), ('C', 'Center'), ('SF', 'Small Forward'), ('PF', 'Power Forward')], 
        label="Initiated By", 
        widget=forms.Select(attrs={"class": "form-control"})
    )
    success = forms.ChoiceField(
        choices=[(1, 'Yes'), (0, 'No')], 
        widget=forms.Select(attrs={"class": "form-control"})
    )
    side = forms.ChoiceField(
        choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')], 
        widget=forms.Select(attrs={"class": "form-control"})
    )
    three_pt_defense_failures = forms.IntegerField(
        label="3pt_defense_failures", 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    three_pt_success_by_opponent = forms.IntegerField(
        label="3pt_success_by_opponent", 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    total_fast_breaks = forms.IntegerField(
        label="total_fast_breaks", 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    game_result = forms.ChoiceField(
        choices=[('win', 'Win'), ('loss', 'Loss')], 
        widget=forms.Select(attrs={"class": "form-control"})
    )