import Link from "next/link";

export default function Home() {
  return (
    <main>
      <div>
        Hello world!
      </div>
      <div>
        <Link href="/test">Test!</Link>
      </div>
    </main>
  );
}
