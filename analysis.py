import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _(np, pd):
    email = "22f3002460@ds.study.iitm.ac.in"
    np.random.seed(0)
    df = pd.DataFrame({
        "X": np.linspace(0, 10, 100),
        "noise": np.random.normal(0, 1, 100)
    })
    df["Y"] = 2 * df["X"] + df["noise"]
    df.head()
    return (df,)


@app.cell
def _():
    return


@app.cell
def _(ui):
    slope_slider = ui.slider(min=0, max=5, step=0.1, value=2.0, label="Select slope")
    slope_slider
    return (slope_slider,)


@app.cell
def _():
    return


@app.cell
def _(df, slope_slider):
    slope = slope_slider.value
    df_pred = df.copy()
    df_pred["Y_pred"] = slope * df_pred["X"]
    df_pred.head()
    return (df_pred,)


@app.cell
def _():
    return


@app.cell
def _(df_pred):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.scatter(df_pred["X"], df_pred["Y"], label="Actual Y", alpha=0.5)
    ax.plot(df_pred["X"], df_pred["Y_pred"], color="red", label="Predicted Y", linewidth=2)
    ax.set_title("Actual vs Predicted Y")
    ax.set_xlabel("X")
    ax.set_ylabel("Y / Y_pred")
    ax.legend()
    plt.show()
    return


@app.cell
def _():
    return


@app.cell
def _(slope_slider):
    slope = slope_slider.value
    f"### The current slope is **{slope:.2f}**. This affects the Y_pred line."
    return


@app.cell
def _():
    # This cell creates a slider to dynamically control slope of Y = mX
    # 22f3002460@ds.study.iitm.ac.in
    # The next cell recomputes predictions based on the slider value

    return


if __name__ == "__main__":
    app.run()
