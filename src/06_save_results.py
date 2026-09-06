import json


results = {
    "estimated_parameters": {
        "theta_degrees": 29.99997293,
        "M": 0.0299999969,
        "X": 54.99999821
    },
    "rounded_parameters": {
        "theta_degrees": 30.0,
        "M": 0.03,
        "X": 55.0
    },
    "optimization": {
        "objective": 1.215331957335e-11,
        "success": True
    },
    "recovered_t_range": {
        "minimum": 6.04940547,
        "maximum": 59.99517070
    },
    "observed_point_validation": {
        "L1_distance": 0.003839680938,
        "MAE": 0.000002559787,
        "RMSE": 0.000003486163,
        "maximum_error": 0.000017617345
    },
    "uniform_parameter_accuracy": {
        "L1_distance": 0.02220975154872,
        "MAE": 0.00001480650103248,
        "RMSE": 0.00001647929279636,
        "maximum_distance": 0.00002686316888372
    }
}


with open("results/parameter_results.json", "w") as file:
    json.dump(results, file, indent=4)


print("Results saved to results/parameter_results.json")