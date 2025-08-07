import marimo

__generated_with = "0.8.18"
app = marimo.App(width="medium")


@app.cell
def __():
    # Email: 22f3002460@ds.study.iitm.ac.in
    # This cell imports necessary libraries and sets up the foundation for our analysis
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    # Set style for better visualizations
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    
    return mo, np, pd, plt, sns


@app.cell
def __(np, pd):
    # Cell 1: Data Generation
    # This cell creates synthetic dataset that will be used by downstream cells
    # The data simulates a relationship between study hours and exam scores
    
    np.random.seed(42)  # For reproducible results
    
    # Generate sample data
    n_samples = 100
    study_hours = np.random.normal(5, 2, n_samples)
    study_hours = np.clip(study_hours, 0, 12)  # Limit to realistic range
    
    # Create exam scores with some correlation to study hours plus noise
    exam_scores = 60 + 3 * study_hours + np.random.normal(0, 10, n_samples)
    exam_scores = np.clip(exam_scores, 0, 100)  # Limit to 0-100 range
    
    # Create DataFrame
    df = pd.DataFrame({
        'study_hours': study_hours,
        'exam_scores': exam_scores,
        'student_id': range(1, n_samples + 1)
    })
    
    print(f"Dataset created with {len(df)} samples")
    print("\nFirst 5 rows:")
    print(df.head())
    
    return df, exam_scores, n_samples, study_hours


@app.cell
def __(mo):
    # Cell 2: Interactive Widget Definition
    # This slider will control the filtering threshold for our analysis
    # Dependent cells will react to changes in this widget
    
    study_hours_threshold = mo.ui.slider(
        start=0, 
        stop=12, 
        step=0.5, 
        value=5.0,
        label="Study Hours Threshold: ",
        show_value=True
    )
    
    return study_hours_threshold,


@app.cell
def __(study_hours_threshold):
    # Cell 3: Display the Interactive Widget
    # This cell shows the slider and provides context about its purpose
    
    mo.md(f"""
    ## Interactive Data Analysis Dashboard
    
    **Control Panel:**
    Use the slider below to filter students based on their study hours.
    Current threshold: **{study_hours_threshold.value} hours**
    
    {study_hours_threshold}
    """)


@app.cell
def __(df, study_hours_threshold):
    # Cell 4: Data Filtering (Dependent on slider widget)
    # This cell depends on both the original dataset (df) and the slider value
    # It demonstrates variable dependency as it reacts to slider changes
    
    # Filter data based on slider value
    filtered_df = df[df['study_hours'] >= study_hours_threshold.value].copy()
    
    # Calculate statistics for filtered data
    filtered_stats = {
        'count': len(filtered_df),
        'mean_hours': filtered_df['study_hours'].mean(),
        'mean_score': filtered_df['exam_scores'].mean(),
        'correlation': filtered_df['study_hours'].corr(filtered_df['exam_scores'])
    }
    
    return filtered_df, filtered_stats


@app.cell
def __(filtered_df, filtered_stats, mo, study_hours_threshold):
    # Cell 5: Dynamic Markdown Output (Dependent on filtered data)
    # This cell creates dynamic content that changes based on the widget state
    # It depends on the filtered data from the previous cell
    
    # Create dynamic content based on current filter
    if len(filtered_df) > 0:
        analysis_text = f"""
        ## Analysis Results
        
        **Filter Applied:** Students with ≥ {study_hours_threshold.value} study hours
        
        ### Summary Statistics:
        - **Students included:** {filtered_stats['count']} out of 100
        - **Average study hours:** {filtered_stats['mean_hours']:.2f} hours
        - **Average exam score:** {filtered_stats['mean_score']:.2f} points
        - **Correlation coefficient:** {filtered_stats['correlation']:.3f}
        
        ### Insights:
        """
        
        if filtered_stats['correlation'] > 0.5:
            insight = "📈 **Strong positive correlation** between study hours and exam scores!"
        elif filtered_stats['correlation'] > 0.3:
            insight = "📊 **Moderate positive correlation** between study hours and exam scores."
        else:
            insight = "📉 **Weak correlation** - other factors may be influencing exam scores."
            
        analysis_text += insight
        
        if filtered_stats['count'] < 20:
            analysis_text += "\n\n⚠️ **Note:** Small sample size - results may not be representative."
            
    else:
        analysis_text = """
        ## No Data Available
        
        ⚠️ No students meet the current criteria. Please lower the threshold.
        """
    
    mo.md(analysis_text)


@app.cell
def __(filtered_df, plt, sns, study_hours_threshold):
    # Cell 6: Dynamic Visualization (Dependent on filtered data)
    # This cell creates a plot that updates based on the filtered dataset
    # Demonstrates how visualizations can be reactive to widget changes
    
    if len(filtered_df) > 0:
        # Create scatter plot with regression line
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Scatter plot of filtered data
        sns.scatterplot(data=filtered_df, x='study_hours', y='exam_scores', 
                       alpha=0.7, s=60, ax=ax)
        
        # Add regression line
        sns.regplot(data=filtered_df, x='study_hours', y='exam_scores', 
                   scatter=False, ax=ax, color='red')
        
        # Customize plot
        ax.set_title(f'Study Hours vs Exam Scores\n(Students with ≥{study_hours_threshold.value} hours)', 
                    fontsize=14, fontweight='bold')
        ax.set_xlabel('Study Hours', fontsize=12)
        ax.set_ylabel('Exam Scores', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Add sample size annotation
        ax.text(0.02, 0.98, f'n = {len(filtered_df)}', transform=ax.transAxes, 
                fontsize=11, verticalalignment='top', 
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        plt.tight_layout()
        plt.show()
    else:
        print("No data to display. Please adjust the threshold.")
    
    return ax, fig


@app.cell
def __(df, mo):
    # Cell 7: Summary Statistics Table (Independent baseline)
    # This cell provides overall dataset statistics as a reference
    # It's independent of the filter but provides context for comparison
    
    summary_stats = df.describe().round(2)
    
    mo.md(f"""
    ## Overall Dataset Summary
    
    **Complete dataset statistics for reference:**
    
    {mo.as_html(summary_stats)}
    
    ---
    
    ### Data Flow Documentation:
    1. **Cell 1**: Library imports and setup
    2. **Cell 2**: Dataset generation (synthetic study hours and exam scores)
    3. **Cell 3**: Interactive slider widget definition
    4. **Cell 4**: Data filtering based on slider value (depends on dataset + widget)
    5. **Cell 5**: Dynamic markdown output (depends on filtered data)
    6. **Cell 6**: Dynamic visualization (depends on filtered data)
    7. **Cell 7**: Summary statistics table (independent reference)
    
    **Variable Dependencies:**
    - `filtered_df` ← depends on `df` and `study_hours_threshold.value`
    - `filtered_stats` ← depends on `filtered_df`
    - Dynamic content ← depends on `filtered_stats` and `study_hours_threshold.value`
    """)


if __name__ == "__main__":
    app.run()
