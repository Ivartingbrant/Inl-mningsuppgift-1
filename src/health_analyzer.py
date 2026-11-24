from src.metrics import (
    summary_stats,
    disease_percentage,
    blood_pressure_ci,
    smoker_bp_difference
)


class HealthAnalyzer:
    """Klass för analys av hälsodata."""

    def __init__(self, df):
        self.df = df

    def summary(self):
        """Returnerar beskrivande statistik."""
        return summary_stats(self.df)

    def disease_percentage(self):
        """Returnerar andelen personer med sjukdom."""
        return disease_percentage(self.df)

    def blood_pressure_ci(self):
        """Returnerar medelblodtryck och 95 % konfidensintervall."""
        return blood_pressure_ci(self.df)

    def smoker_bp_difference(self):
        """Returnerar skillnaden i medelblodtryck mellan grupperna."""
        return smoker_bp_difference(self.df)
