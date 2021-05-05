import useSWR from "swr";

export default function useCars(backendUrl, user) {
  const { data: cars } = useSWR(user?.code == 200 && `${backendUrl}/api/car`);

  const loadingCars = cars === undefined;

  return { cars, loadingCars };
}
