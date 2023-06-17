from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import CronSchedule
from prefect.flow_runners import SubprocessFlowRunner
# from score import ride_duration_prediction

# deployment = Deployment.build_from_flow(
#     flow=ride_duration_prediction,
#     name="ride_duration_prediction",
#     parameters={
#         "taxi_type": "green",
#         "run_id": "db63d368b9b34a7d9ef277929c04c78d",
#     },
#     schedule=CronSchedule(cron="0 3 2 * *"),
#     work_queue_name="ml",
# )
# deployment.apply()

DeploymentSpec(
    flow_location='score.py',
    name="ride_duration_prediction",
    parameters={
        "taxi_type": "green",
        "run_id": "db63d368b9b34a7d9ef277929c04c78d",
    },
    schedule=CronSchedule(cron="0 3 2 * *"),
    flow_runner=SubprocessFlowRunner(),
    tags=["ml"],
)


