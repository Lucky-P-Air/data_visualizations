from sjvisualizer import DataHandler, BarRace, Canvas, PieRace, StaticImage

EXCEL_FILENAME = "data/cumulative_space_visits_processed.xlsx"
STATIC_IMAGE_FILE = "assets/iss.png"
FPS = 60
DURATION = 12  # seconds
TITLE_BARRACE = "Cumulative Number of Humans to Visit Space"
SUBTITLE_BARRACE = "1961 - 2021"
BG_COLOR = (255, 255, 255)
BAR_COLORS = {'Total': (67, 160, 71),
              'Americans': (30, 136, 229),
              'Russians': (244, 67, 54),
              'Misc': (253, 216, 53),
              'Japanese': (96, 125, 139)}
CITATION = 'Source: CSIS Aerospace Security Project (2022)'
WIDTH = 2000  # Canvas size
HEIGHT = 1200  # Canvas size

# Load Excel data into Pandas dataframe
df = DataHandler.DataHandler(excel_file=EXCEL_FILENAME, number_of_frames=FPS*DURATION).df

# Create a canvas for the plots
base_canvas = Canvas.canvas(width=WIDTH, height=HEIGHT, bg=BG_COLOR)
base_canvas.tk.attributes("-fullscreen", True)

# Create bar chart
bar_chart = BarRace.bar_race(df=df, canvas=base_canvas.canvas,
                             width=WIDTH*.8, height=HEIGHT*.6,
                             x_pos=WIDTH*.1, y_pos=HEIGHT*.15,
                             colors=BAR_COLORS, text=CITATION,
                             back_ground_color=BG_COLOR)
base_canvas.add_sub_plot(bar_chart)

# Add chart details
base_canvas.add_time(df=df, time_indicator='year', color=(150, 150, 150))
base_canvas.add_title(text=TITLE_BARRACE, color=(150, 150, 150))
base_canvas.add_sub_title(text=SUBTITLE_BARRACE, color=(179, 190, 197))
base_canvas.canvas.create_text(WIDTH / 2, HEIGHT * .95, text=CITATION)
# base_canvas.add_logo(logo='assets/logo2.png')
# Add subplot to canvas
base_canvas.add_sub_plot(bar_chart)

# Adding a PIP chart & static image
pip_chart = PieRace.pie_plot(df=df.drop('Total', axis=1), canvas=base_canvas.canvas,
                             width=WIDTH*.18, height=WIDTH*.18, x_pos=WIDTH*.7, y_pos=HEIGHT*.42,
                             colors=BAR_COLORS, back_ground_color=BG_COLOR)
base_canvas.add_sub_plot(pip_chart)
iss_image = StaticImage.static_image(canvas=base_canvas.canvas,
                                     width=130, height=74,
                                     x_pos=WIDTH*.85, y_pos=HEIGHT/30,
                                     file=STATIC_IMAGE_FILE)
base_canvas.add_sub_plot(iss_image)

if __name__ == '__main__':
    base_canvas.play(fps=FPS)
