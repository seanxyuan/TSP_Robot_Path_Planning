from constant import EDGE_TPYE

def get_edge_cost(edge_data):
    if 'ROTATION_COST' in edge_data:
        return edge_data['ROTATION_COST']
    elif 'IDLE_COST' in edge_data:
        return edge_data['IDLE_COST']
    else:
        return edge_data['DEPOSITION_COST']

def get_edge_type_cost(edge_data):
    type = ''
    cost = 0

    if 'DEPOSITION_COST' in edge_data:
        type = EDGE_TPYE.DEPOSITION
        cost = edge_data['DEPOSITION_COST']
    else:
        if 'ROTATION_COST' in edge_data:
            type = EDGE_TPYE.ROTATION
            cost = edge_data['ROTATION_COST']
        elif 'IDLE_COST' in edge_data:
            type = EDGE_TPYE.IDLE
            cost =  edge_data['IDLE_COST']

    return {
        'type': type,
        'cost': cost
    }
