import useSWR from "swr";

export default function useTokens(backendUrl, user) {
  const { data: tokens } = useSWR(
    user?.code == 200 && `${backendUrl}/api/token`
  );

  const loadingTokens = tokens === undefined;

  return { tokens, loadingTokens };
}
