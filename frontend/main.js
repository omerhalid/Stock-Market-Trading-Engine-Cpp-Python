// https://v0.dev/t/23zbHnDtOAe

/**
 * v0 by Vercel.
 * @see https://v0.dev/t/23zbHnDtOAe
 */
import Link from "next/link"
import { ResponsiveLine } from "@nivo/line"
import { CardTitle, CardDescription, CardHeader, Card, CardContent, CardFooter } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { CollapsibleTrigger, CollapsibleContent, Collapsible } from "@/components/ui/collapsible"
import { Input } from "@/components/ui/input"

export default function Component() {
  return (
    <div className="flex flex-col min-h-screen">
      <header className="px-4 lg:px-6 h-14 flex items-center fixed w-full z-10 bg-white">
        <Link className="flex items-center justify-center" href="#">
          <PlaneIcon className="h-6 w-6" />
          <span className="sr-only">Stock Engine</span>
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#">
            About
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#">
            Features
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#">
            Testimonials
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#">
            Pricing
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#">
            FAQ
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#">
            Contact
          </Link>
        </nav>
      </header>
      <main className="flex-1 mt-14">
        <section className="w-full pt-12 md:pt-24 lg:pt-32 border-y">
          <div className="px-4 md:px-6 space-y-10 xl:space-y-16">
            <div className="grid max-w-[1300px] mx-auto gap-4 px-4 sm:px-6 md:px-10 md:grid-cols-2 md:gap-16">
              <div>
                <h1 className="lg:leading-tighter text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl xl:text-[3.4rem] 2xl:text-[3.75rem]">
                  Real-time Stock Market Trading Engine
                </h1>
                <p className="mx-auto max-w-[700px] text-gray-500 md:text-xl dark:text-gray-400">
                  Get access to real-time market data, advanced trading tools, and a seamless user experience. Our
                  complex algorithms decide when to buy or sell for optimal results.
                </p>
                <div className="space-x-4">
                  <Link
                    className="inline-flex h-9 items-center justify-center rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-gray-50 shadow transition-colors hover:bg-gray-900/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:bg-gray-50 dark:text-gray-900 dark:hover:bg-gray-50/90 dark:focus-visible:ring-gray-300"
                    href="#"
                  >
                    Get Started
                  </Link>
                </div>
              </div>
              <div>
                <CurvedlineChart className="w-full aspect-[4/3]" />
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32" id="about">
          <div className="container space-y-12 px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <div className="inline-block rounded-lg bg-gray-100 px-3 py-1 text-sm dark:bg-gray-800">About</div>
                <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">
                  Real-time Market Data and Advanced Trading Algorithms
                </h2>
                <p className="max-w-[900px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                  Our Stock Market Trading Engine provides real-time market data and uses advanced algorithms to decide
                  when to buy or sell for optimal results. Enjoy a seamless user experience to help you make informed
                  trading decisions.
                </p>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-100 dark:bg-gray-800" id="features">
          <div className="container grid items-center justify-center gap-4 px-4 text-center md:px-6">
            <div className="space-y-3">
              <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight">Key Features</h2>
              <p className="mx-auto max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                Experience the best trading solutions with our innovative features.
              </p>
            </div>
            <div className="mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-4">
              <div>
                <PlaneIcon className="w-4 h-4 mb-4" />
                <h3 className="text-lg font-bold">Real-time Stock Quotes</h3>
                <p className="text-sm text-gray-500 dark:text-gray-400">Get real-time stock quotes and market data.</p>
              </div>
              <div>
                <PlaneIcon className="w-4 h-4 mb-4" />
                <h3 className="text-lg font-bold">Customizable Watchlists</h3>
                <p className="text-sm text-gray-500 dark:text-gray-400">
                  Create and customize watchlists to track your favorite stocks.
                </p>
              </div>
              <div>
                <PlaneIcon className="w-4 h-4 mb-4" />
                <h3 className="text-lg font-bold">Advanced Charting Tools</h3>
                <p className="text-sm text-gray-500 dark:text-gray-400">
                  Use advanced charting tools to analyze market trends.
                </p>
              </div>
              <div>
                <PlaneIcon className="w-4 h-4 mb-4" />
                <h3 className="text-lg font-bold">Complex Trading Algorithms</h3>
                <p className="text-sm text-gray-500 dark:text-gray-400">
                  Our advanced algorithms decide when to buy or sell for optimal trading results.
                </p>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32" id="testimonials">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <div className="inline-block rounded-lg bg-gray-100 px-3 py-1 text-sm dark:bg-gray-800">
                  Testimonials
                </div>
                <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">Trusted by Professionals Worldwide</h2>
                <p className="max-w-[900px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                  Hear what our satisfied customers have to say about our Stock Market Trading Engine.
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-2">
              <Card>
                <CardHeader>
                  <CardTitle>John Doe</CardTitle>
                  <CardDescription>
                    "The real-time market data and advanced trading algorithms provided by the Stock Market Trading
                    Engine have significantly improved my trading decisions. Highly recommended!"
                  </CardDescription>
                </CardHeader>
              </Card>
              <Card>
                <CardHeader>
                  <CardTitle>Jane Smith</CardTitle>
                  <CardDescription>
                    "The complex trading strategies feature has helped me maximize my profits. The user experience is
                    seamless and intuitive. Great job!"
                  </CardDescription>
                </CardHeader>
              </Card>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-100 dark:bg-gray-800" id="pricing">
          <div className="container grid items-center justify-center gap-6 px-4 md:px-6 lg:grid-cols-3 lg:gap-10">
            <div className="space-y-2">
              <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight">Pricing Plans</h2>
              <p className="max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                Choose the best plan that fits your trading needs.
              </p>
            </div>
            <Card>
              <CardHeader>
                <CardTitle>Basic</CardTitle>
                <CardDescription>$10/month</CardDescription>
              </CardHeader>
              <CardContent>
                Real-time Stock Quotes
                <br />
                Customizable Watchlists
              </CardContent>
              <CardFooter>
                <Button>Choose Plan</Button>
              </CardFooter>
            </Card>
            <Card>
              <CardHeader>
                <CardTitle>Premium</CardTitle>
                <CardDescription>$20/month</CardDescription>
              </CardHeader>
              <CardContent>
                Real-time Stock Quotes
                <br />
                Customizable Watchlists
                <br />
                Advanced Charting Tools
              </CardContent>
              <CardFooter>
                <Button>Choose Plan</Button>
              </CardFooter>
            </Card>
            <Card>
              <CardHeader>
                <CardTitle>Pro</CardTitle>
                <CardDescription>$30/month</CardDescription>
              </CardHeader>
              <CardContent>
                Real-time Stock Quotes
                <br />
                Customizable Watchlists
                <br />
                Advanced Charting Tools
                <br />
                Complex Trading Algorithms
              </CardContent>
              <CardFooter>
                <Button>Choose Plan</Button>
              </CardFooter>
            </Card>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32" id="faq">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <div className="inline-block rounded-lg bg-gray-100 px-3 py-1 text-sm dark:bg-gray-800">FAQ</div>
                <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">Frequently Asked Questions</h2>
                <p className="max-w-[900px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                  Here are some answers to the most commonly asked questions about our Stock Market Trading Engine.
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl items-center gap-6 py-12 lg:grid-cols-2">
              <Collapsible className="w-full">
                <CollapsibleTrigger className="flex justify-between items-center px-4 py-2">
                  What is the Stock Market Trading Engine?
                  <ChevronDownIcon className="w-4 h-4" />
                </CollapsibleTrigger>
                <CollapsibleContent className="px-4 py-2">
                  The Stock Market Trading Engine is a platform that provides real-time market data and uses advanced
                  algorithms to decide when to buy or sell for optimal results. Enjoy a seamless user experience to help
                  you make informed trading decisions.
                </CollapsibleContent>
              </Collapsible>
              <Collapsible className="w-full">
                <CollapsibleTrigger className="flex justify-between items-center px-4 py-2">
                  How do I sign up?
                  <ChevronDownIcon className="w-4 h-4" />
                </CollapsibleTrigger>
                <CollapsibleContent className="px-4 py-2">
                  Click on the "Get Started" button on the homepage to sign up for an account.
                </CollapsibleContent>
              </Collapsible>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-100 dark:bg-gray-800" id="contact">
          <div className="container grid items-center justify-center gap-6 px-4 md:px-6 lg:grid-cols-2 lg:gap-10">
            <div className="space-y-2">
              <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight">Contact Us</h2>
              <p className="max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                If you have any questions or need further assistance, feel free to get in touch with us.
              </p>
            </div>
            <form className="w-full max-w-sm space-y-2">
              <Input placeholder="Name" type="text" />
              <Input placeholder="Email" type="email" />
              <textarea className="w-full h-24 px-3 py-2 border rounded-md" placeholder="Message" />
              <Button>Submit</Button>
            </form>
          </div>
        </section>
      </main>
      <footer className="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t">
        <p className="text-xs text-gray-500 dark:text-gray-400">© Stock Engine Inc. All rights reserved.</p>
        <nav className="sm:ml-auto flex gap-4 sm:gap-6">
          <Link className="text-xs hover:underline underline-offset-4" href="#">
            Terms of Service
          </Link>
          <Link className="text-xs hover:underline underline-offset-4" href="#">
            Privacy
          </Link>
          <Link className="text-xs hover:underline underline-offset-4" href="#">
            Disclaimer
          </Link>
        </nav>
      </footer>
    </div>
  )
}

function ChevronDownIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m6 9 6 6 6-6" />
    </svg>
  )
}


function CurvedlineChart(props) {
  return (
    <div {...props}>
      <ResponsiveLine
        data={[
          {
            id: "B",
            data: [
              { x: "2018-01-01", y: 7 },
              { x: "2018-01-02", y: 5 },
              { x: "2018-01-03", y: 11 },
              { x: "2018-01-04", y: 9 },
              { x: "2018-01-05", y: 12 },
              { x: "2018-01-06", y: 16 },
              { x: "2018-01-07", y: 13 },
              { x: "2018-01-08", y: 13 },
            ],
          },
          {
            id: "A",
            data: [
              { x: "2018-01-01", y: 9 },
              { x: "2018-01-02", y: 8 },
              { x: "2018-01-03", y: 13 },
              { x: "2018-01-04", y: 6 },
              { x: "2018-01-05", y: 8 },
              { x: "2018-01-06", y: 14 },
              { x: "2018-01-07", y: 11 },
              { x: "2018-01-08", y: 12 },
            ],
          },
        ]}
        enableCrosshair={false}
        margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
        xScale={{
          type: "time",
          format: "%Y-%m-%d",
          useUTC: false,
          precision: "day",
        }}
        xFormat="time:%Y-%m-%d"
        yScale={{
          type: "linear",
          min: 0,
          max: "auto",
        }}
        axisTop={null}
        axisRight={null}
        axisBottom={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 0,
          legend: "X",
          legendOffset: 45,
          legendPosition: "middle",
          format: "%b %d",
          tickValues: "every 1 day",
        }}
        axisLeft={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 0,
          legend: "Y",
          legendOffset: -45,
          legendPosition: "middle",
        }}
        colors={{ scheme: "paired" }}
        pointSize={5}
        pointColor={{
          from: "color",
          modifiers: [["darker", 0.2]],
        }}
        pointBorderWidth={2}
        pointBorderColor={{
          from: "color",
          modifiers: [["darker", 0.2]],
        }}
        pointLabelYOffset={-12}
        useMesh={true}
        curve="monotoneX"
        legends={[
          {
            anchor: "bottom-right",
            direction: "column",
            justify: false,
            translateX: 100,
            translateY: 0,
            itemsSpacing: 0,
            itemDirection: "left-to-right",
            itemWidth: 80,
            itemHeight: 20,
            symbolSize: 14,
            symbolShape: "circle",
          },
        ]}
        theme={{
          tooltip: {
            container: {
              fontSize: "12px",
            },
          },
        }}
        role="application"
      />
    </div>
  )
}


function PlaneIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z" />
    </svg>
  )
}
