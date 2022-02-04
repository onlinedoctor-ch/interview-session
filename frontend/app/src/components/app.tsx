import * as React from "react";
import { DoctorsList } from "./DoctorsList";
import { ChakraProvider, Flex, Heading, Text } from "@chakra-ui/react";
import { HealthChecker } from "./HealthChecker";

export const App: React.FC = () => {
  return (
    <ChakraProvider>
      <Layout>
        <DoctorsList />
        <HealthChecker />
      </Layout>
    </ChakraProvider>
  );
};

export const Layout: React.FC<React.PropsWithChildren<{}>> = ({ children }) => {
  return (
    <Flex flexDir="column" height="100%">
      <Flex flexDir="row" bgColor="teal" p={4}>
        <Heading color="white">OnlineDoctor</Heading>
      </Flex>
      <Flex flexDir="column" p={4} flex={1} overflowY="auto">
        {children}
      </Flex>
      <Flex
        flexDir="column"
        bgColor="teal"
        color="whitesmoke"
        p={4}
        justifyContent="center"
        alignItems="center"
      >
        <Heading size="sm">Made with ☕</Heading>
        <Text fontSize="sm">@OnlineDoctor</Text>
      </Flex>
    </Flex>
  );
};
