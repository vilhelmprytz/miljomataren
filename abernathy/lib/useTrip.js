import useSWR from "swr";

export default function useTrip(backendUrl, user, tripId) {
  const { data: trip } = useSWR(
    user?.code == 200 && `${backendUrl}/api/trip/${tripId}`
  );

  const loadingTrip = trip === undefined;

  return { trip, loadingTrip };
}
