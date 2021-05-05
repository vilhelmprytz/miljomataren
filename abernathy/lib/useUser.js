import { useEffect } from "react";
import Router from "next/router";
import useSWR from "swr";

export default function useUser({
  backendUrl = "",
  redirectTo = false,
  redirectIfFound = false,
} = {}) {
  const { data: user, mutate: mutateUser } = useSWR(`${backendUrl}/api/user`);

  useEffect(() => {
    // if no redirect needed, just return (example: already on /dashboard)
    // if user data not yet there (fetch in progress, logged in or not) then don't do anything yet

    if (!redirectTo || !user) return;

    if (
      // If redirectTo is set, redirect if the user was not found.
      (redirectTo && !redirectIfFound && !user?.code == 200) ||
      // If redirectIfFound is also set, redirect if the user was found
      (redirectIfFound && user?.code == 200)
    ) {
      Router.push(redirectTo);
    }
  }, [user, redirectIfFound, redirectTo]);

  return { user, mutateUser };
}
