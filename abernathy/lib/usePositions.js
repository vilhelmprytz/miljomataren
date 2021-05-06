import useSWR from "swr";

export default function usePositions(backendUrl, user, tripId) {
  const { data: positions } = useSWR(
    user?.code == 200 && `${backendUrl}/api/position?trip_id=${tripId}`
  );

  const loadingPositions = positions === undefined;

  return { positions, loadingPositions };
}
