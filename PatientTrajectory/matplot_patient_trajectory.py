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
        # original_df = original_df.sort_values(by=["pasient"])
        original_df = original_df.sort_values(by=["initial_age", "Length_of_Episode"])

        return original_df

    def patient_timeline_plot_yearly(self, original_df, ax, cmap, unique_patients):
        for i, patient_id in enumerate(unique_patients):
            patient_data = original_df[original_df["pasient"] == patient_id]
            for _, case in patient_data.iterrows():
                case_start = case["episode_start_date"]
                case_end = case["episode_end_date"]
                case_count_visit = case["Count_visit"]
                case_age = case["age"]
                case_diag = case["diagnosis"]
                case_cluster = case["cluster"]
                case_medication = case["actual_med_Full_ATC"]
                # Round case_age to 1 decimal float only
                label_demographics = f"{round(case_age, 1)} : {case_cluster}: {case_count_visit}: {case_medication} :{case_diag} "
                # label_diagnosis = f"{case_medication} :{case_diag}"
                age_start = case_age
                age_end = age_start + (case_end - case_start).days / 365.2425

                ax.plot(
                    [age_start, age_end],
                    [i, i],
                    linewidth=5,
                    color=cmap[case_cluster],
                )
                ax.annotate(
                    label_demographics,
                    (age_start + 0.01, i),
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

        ax.set_yticks(range(len(unique_patients)))
        ax.set_yticklabels(unique_patients)

        min_age = int(original_df["age"].min())
        ax.set_xticks(range(min_age, 18, 2))
        ax.set_xlim(min_age - 0.1, 18)

        ax.grid(True, linewidth=0.05)
        ax.set_xlabel("Age at Episode of Care")
        ax.set_ylabel("Patient ID")


# To verify middle childhood are not less then 6 years old
class MatplotlibPatientTrajectoryMiddleChildhood:
    def load_data(self, original_df):
        original_df = original_df
        original_df["episode_start_date"] = pd.to_datetime(
            original_df["episode_start_date"]
        )
        original_df["episode_end_date"] = pd.to_datetime(
            original_df["episode_end_date"], errors="coerce"
        )
        # original_df = original_df.sort_values(by=["pasient"])
        original_df = original_df.sort_values(by=["initial_age", "Length_of_Episode"])
        return original_df

    def patient_timeline_plot_yearly(self, original_df, ax, cmap, unique_patients):
        for i, patient_id in enumerate(unique_patients):
            patient_data = original_df[original_df["pasient"] == patient_id]
            for _, case in patient_data.iterrows():
                case_start = case["episode_start_date"]
                case_end = case["episode_end_date"]
                case_count_visit = case["Count_visit"]
                case_age = case["age"]
                case_diag = case["diagnosis"]
                case_cluster = case["cluster"]
                case_medication = case["actual_med_Full_ATC"]
                # Round case_age to 1 decimal float only
                label_demographics = f"{round(case_age, 1)} : {case_cluster}: {case_count_visit}: {case_medication} :{case_diag} "
                # label_diagnosis = f"{case_medication} :{case_diag}"
                age_start = case_age
                age_end = age_start + (case_end - case_start).days / 365.2425

                ax.plot(
                    [age_start, age_end],
                    [i, i],
                    linewidth=5,
                    color=cmap[case_cluster],
                )
                ax.annotate(
                    label_demographics,
                    (age_start + 0.01, i),
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

        ax.set_yticks(range(len(unique_patients)))
        ax.set_yticklabels(unique_patients)

        min_age = int(original_df["age"].min())
        ax.set_xticks(range(min_age, 18, 2))
        ax.set_xlim(min_age - 0.1, 18)

        ax.grid(True, linewidth=0.05)
        ax.set_xlabel("Age at Episode of Care")
        ax.set_ylabel("Patient ID")


# To verify teenager are not less then 12 years old
class MatplotlibPatientTrajectoryTeenager:

    def load_data(self, original_df):
        original_df = original_df
        original_df["episode_start_date"] = pd.to_datetime(
            original_df["episode_start_date"]
        )
        original_df["episode_end_date"] = pd.to_datetime(
            original_df["episode_end_date"], errors="coerce"
        )
        # original_df = original_df.sort_values(by=["pasient"])
        original_df = original_df.sort_values(by=["initial_age", "Length_of_Episode"])
        return original_df

    def patient_timeline_plot_yearly(self, original_df, ax, cmap, unique_patients):
        for i, patient_id in enumerate(unique_patients):
            patient_data = original_df[original_df["pasient"] == patient_id]
            for _, case in patient_data.iterrows():
                case_start = case["episode_start_date"]
                case_end = case["episode_end_date"]
                case_count_visit = case["Count_visit"]
                case_age = case["age"]
                case_diag = case["diagnosis"]
                case_cluster = case["cluster"]
                case_medication = case["actual_med_Full_ATC"]
                # Round case_age to 1 decimal float only
                label_demographics = f"{round(case_age, 1)} : {case_cluster}: {case_count_visit}: {case_medication} :{case_diag} "
                # label_diagnosis = f"{case_medication} :{case_diag}"
                age_start = case_age
                age_end = age_start + (case_end - case_start).days / 365.2425

                ax.plot(
                    [age_start, age_end],
                    [i, i],
                    linewidth=5,
                    color=cmap[case_cluster],
                )
                ax.annotate(
                    label_demographics,
                    (age_start + 0.01, i),
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

        ax.set_yticks(range(len(unique_patients)))
        ax.set_yticklabels(unique_patients)
        min_age = int(original_df["age"].min())
        ax.set_xticks(range(min_age, 18, 2))
        ax.set_xlim(min_age - 0.1, 18)

        ax.grid(True, linewidth=0.05)
        ax.set_xlabel("Age at Episode of Care")
        ax.set_ylabel("Patient ID")
