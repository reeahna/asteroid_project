from paraview.simple import *

# -------------------------------------------------------------------------
# GET EXISTING SOURCES
# -------------------------------------------------------------------------
A31 = FindSource("A31")
B31 = FindSource("B31")
A11 = FindSource("A11")

print("Loaded:", A31, B31, A11)

# -------------------------------------------------------------------------
# GET EXISTING VIEWS
# -------------------------------------------------------------------------
views = GetRenderViews()

if len(views) < 3:
    print("ERROR: You must create 3 render views first.")
    raise SystemExit

view1, view2, view3 = views[0], views[1], views[2]

print("Using views:", view1, view2, view3)

# -------------------------------------------------------------------------
# HELPER FUNCTION
# -------------------------------------------------------------------------
def buildScene(simSource, renderView):

    HideAll()

    # ---- WATER SURFACE ----
    water = Contour(Input=simSource)
    water.ContourBy = ['POINTS', 'v02']
    water.Isosurfaces = [0.5]
    wDisp = Show(water, renderView)
    wDisp.DiffuseColor = [0.1, 0.3, 1.0]
    wDisp.Opacity = 0.4

    # ---- ASTEROID ----
    asteroid = Contour(Input=simSource)
    asteroid.ContourBy = ['POINTS', 'v03']
    asteroid.Isosurfaces = [0.5]
    aDisp = Show(asteroid, renderView)
    aDisp.DiffuseColor = [0.4, 0.4, 0.4]

    return (water, asteroid)

# -------------------------------------------------------------------------
# BUILD PANELS
# -------------------------------------------------------------------------

A31_w, A31_a = buildScene(A31, view1)
B31_w, B31_a = buildScene(B31, view2)
A11_w, A11_a = buildScene(A11, view3)

# -------------------------------------------------------------------------
# SYNC CAMERAS
# -------------------------------------------------------------------------
def copy_camera(src, dst):
    dst.CameraPosition = src.CameraPosition
    dst.CameraFocalPoint = src.CameraFocalPoint
    dst.CameraViewUp = src.CameraViewUp
    dst.CameraParallelScale = src.CameraParallelScale

copy_camera(view1, view2)
copy_camera(view1, view3)

# -------------------------------------------------------------------------
# TIME STEP
# -------------------------------------------------------------------------
anim = GetAnimationScene()
tk = GetTimeKeeper()

timestep_index = 30
anim.AnimationTime = tk.TimestepValues[timestep_index]

# -------------------------------------------------------------------------
# RENDER
# -------------------------------------------------------------------------

RenderAllViews()
print("FINISHED: Question 1 layout built successfully.")
