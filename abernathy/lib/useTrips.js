import useSWR from "swr";

export default function useTrips(backendUrl, user) {
  const { data: trips } = useSWR(user?.code == 200 && `${backendUrl}/api/trip`);

  const loadingTrips = trips === undefined;

  return { trips, loadingTrips };
}
