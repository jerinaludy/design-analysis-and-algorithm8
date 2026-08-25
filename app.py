import streamlit as st
from itertools import permutations

INF = float("inf")


def tsp_brute_force(cost, n):
    """Find optimal TSP tour using brute force."""
    cities = list(range(1, n))
    best_cost = INF
    best_path = None

    for perm in permutations(cities):
        path = [0] + list(perm) + [0]

        total_cost = sum(
            cost[path[i]][path[i + 1]]
            for i in range(n)
        )

        if total_cost < best_cost:
            best_cost = total_cost
            best_path = path

    return best_path, best_cost


# -----------------------------
# Streamlit Page Configuration
# -----------------------------

st.set_page_config(
    page_title="5-City TSP",
    page_icon="🗺️",
    layout="centered"
)

st.title("🗺️ 5-City Travelling Salesman Problem")
st.write(
    "This application finds the minimum-cost tour for a "
    "5-city Travelling Salesman Problem using brute force."
)

# -----------------------------
# City Names
# -----------------------------

cities = ["A", "B", "C", "D", "E"]

# -----------------------------
# Cost Matrix
# -----------------------------

cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

# -----------------------------
# Display Cost Matrix
# -----------------------------

st.subheader("📊 Cost Matrix")

display_matrix = []

for i in range(len(cost)):
    row = []

    for j in range(len(cost[i])):
        if cost[i][j] == INF:
            row.append("INF")
        else:
            row.append(cost[i][j])

    display_matrix.append(row)

st.dataframe(
    {
        cities[i]: display_matrix[i]
        for i in range(len(cities))
    },
    use_container_width=True
)

# -----------------------------
# Calculate TSP
# -----------------------------

if st.button("🚀 Find Optimal Tour", use_container_width=True):

    best_path, best_cost = tsp_brute_force(cost, len(cities))

    # Convert numeric path to city names
    city_path = [
        cities[i]
        for i in best_path
    ]

    tour = " → ".join(city_path)

    # -----------------------------
    # Display Result
    # -----------------------------

    st.success("Optimal Tour Found!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Minimum Cost",
            best_cost
        )

    with col2:
        st.metric(
            "Number of Cities",
            len(cities)
        )

    st.subheader("🏆 Optimal Tour")

    st.info(tour)

    # -----------------------------
    # Path Verification
    # -----------------------------

    st.subheader("🔍 Path Verification")

    verification = []

    for i in range(len(cities)):
        u = best_path[i]
        v = best_path[i + 1]

        verification.append({
            "From": cities[u],
            "To": cities[v],
            "Cost": cost[u][v]
        })

    st.dataframe(
        verification,
        use_container_width=True
    )

    # -----------------------------
    # Explanation
    # -----------------------------

    st.subheader("📖 Result Explanation")

    st.write(
        f"The salesman starts from city **{cities[best_path[0]]}**, "
        f"visits every city exactly once, and finally returns to "
        f"city **{cities[best_path[-1]]}**."
    )

    st.write(
        f"The minimum possible travel cost is **{best_cost}**."
    )

    st.write(
        "The brute-force algorithm checks all possible tours "
        "and selects the tour with the smallest total cost."
    )
