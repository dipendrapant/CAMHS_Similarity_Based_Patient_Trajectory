import warnings

warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import Image, display


class MatplotlibPatientTrajectory:
    def load_data(self, original_df):
        original_df = original_df
        original_df["episode_start_date"] = pd.to_datetime(
            original_df["episode_start_date"]
        )
        original_df["episode_end_date"] = pd.to_datetime(
            original_df["episode_end_date"], errors="coerce"
        )
        original_df = original_df.sort_values(by=["pasient", "episode_start_date"])
        return original_df

    def patient_timeline_plot_yearly(self, original_df, ax, cmap, unique_patients):
        for i, patient_id in enumerate(unique_patients):
            patient_data = original_df[original_df["pasient"] == patient_id]
            for _, case in patient_data.iterrows():
                case_start = case["episode_start_date"]
                case_end = case["episode_end_date"]
                case_gender = case["gender"]
                case_age = case["age"]
                case_diag = case["diagnosis"]
                case_cluster = case["cluster"]
                case_medication = case["actual_med_Full_ATC"]
                label_demographics = f"{case_age} : {case_gender} : {case_cluster} "
                label_diagnosis = f"{case_medication} :{case_diag}"
                ax.plot(
                    [case_start, case_end],
                    [i, i],
                    linewidth=5,
                    color=cmap[case_cluster],
                )
                ax.annotate(
                    label_demographics,
                    (case_start + pd.DateOffset(days=2), i),
                    xytext=(0, 7),
                    textcoords="offset points",
                    ha="left",
                    fontsize=8,
                    bbox=dict(
                        boxstyle="round,pad=0.05",
                        edgecolor="grey",
                        linewidth=0.1,
                        facecolor="white",
                    ),
                )
                ax.annotate(
                    label_diagnosis,
                    (case_start + pd.DateOffset(days=2), i),
                    xytext=(0, -12),
                    textcoords="offset points",
                    ha="left",
                    fontsize=8,
                    bbox=dict(
                        boxstyle="round,pad=0.001",
                        edgecolor="grey",
                        linewidth=0.1,
                        facecolor="white",
                    ),
                )

        ax.set_yticks(range(len(unique_patients)))
        ax.set_xlim(
            original_df["episode_start_date"].min(),
            original_df["episode_end_date"].max(),
        )
        ax.set_yticklabels(unique_patients)
        ax.grid(True, linewidth=0.05)
        ax.set_xlabel("Actual Date of Episode of Care")
        ax.set_ylabel("Patient ID")
        ax.xaxis_date()
