import Link from "next/link";

export default function Navbar() {
  return (
    <>
      <Link href="/">
        <button>Home</button>
      </Link>
      <Link href="/car">
        <button>My Cars</button>
      </Link>
      <Link href="/token">
        <button>My Tokens</button>
      </Link>
    </>
  );
}
