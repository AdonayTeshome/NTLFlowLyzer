#!/usr/bin/env python3

from datetime import datetime
from .features import *
import warnings

class FeatureExtractor(object):
    def __init__(self, floating_point_unit: str):
        warnings.filterwarnings("ignore")

        self.floating_point_unit = floating_point_unit
        self.__features = [
                Duration(),
                PacketsCount(),
                FwdPacketsCount(),
                BwdPacketsCount(),

                TotalPayloadBytes(),
                FwdTotalPayloadBytes(),
                BwdTotalPayloadBytes(),
                PayloadBytesMax(),
                PayloadBytesMin(),
                PayloadBytesMean(),
                PayloadBytesStd(),
                PayloadBytesVariance(),
                PayloadBytesMedian(),
                PayloadBytesSkewness(),
                PayloadBytesCov(),
                PayloadBytesMode(),
                FwdPayloadBytesMax(),
                FwdPayloadBytesMin(),
                FwdPayloadBytesMean(),
                FwdPayloadBytesStd(),
                FwdPayloadBytesVariance(),
                FwdPayloadBytesMedian(),
                FwdPayloadBytesSkewness(),
                FwdPayloadBytesCov(),
                FwdPayloadBytesMode(),
                BwdPayloadBytesMax(),
                BwdPayloadBytesMin(),
                BwdPayloadBytesMean(),
                BwdPayloadBytesStd(),
                BwdPayloadBytesVariance(),
                BwdPayloadBytesMedian(),
                BwdPayloadBytesSkewness(),
                BwdPayloadBytesCov(),
                BwdPayloadBytesMode(),

                TotalHeaderBytes(),
                MaxHeaderBytes(),
                MinHeaderBytes(),
                MeanHeaderBytes(),
                StdHeaderBytes(),
                MedianHeaderBytes(),
                SkewnessHeaderBytes(),
                CoVHeaderBytes(),
                ModeHeaderBytes(),
                VarianceHeaderBytes(),
                FwdTotalHeaderBytes(),
                FwdMaxHeaderBytes(),
                FwdMinHeaderBytes(),
                FwdMeanHeaderBytes(),
                FwdStdHeaderBytes(),
                FwdMedianHeaderBytes(),
                FwdSkewnessHeaderBytes(),
                FwdCoVHeaderBytes(),
                FwdModeHeaderBytes(),
                FwdVarianceHeaderBytes(),
                BwdTotalHeaderBytes(),
                BwdMaxHeaderBytes(),
                BwdMinHeaderBytes(),
                BwdMeanHeaderBytes(),
                BwdStdHeaderBytes(),
                BwdMedianHeaderBytes(),
                BwdSkewnessHeaderBytes(),
                BwdCoVHeaderBytes(),
                BwdModeHeaderBytes(),
                BwdVarianceHeaderBytes(),

                FwdAvgSegmentSize(),
                BwdAvgSegmentSize(),
                AvgSegmentSize(),
                FwdInitWinBytes(),
                BwdInitWinBytes(),

                ActiveMin(),
                ActiveMax(),
                ActiveMean(),
                ActiveStd(),
                ActiveMedian(),
                ActiveSkewness(),
                ActiveCoV(),
                ActiveMode(),
                ActiveVariance(),

                IdleMin(),
                IdleMax(),
                IdleMean(),
                IdleStd(),
                IdleMedian(),
                IdleSkewness(),
                IdleCoV(),
                IdleMode(),
                IdleVariance(),

                BytesRate(),
                FwdBytesRate(),
                BwdBytesRate(),
                PacketsRate(),
                BwdPacketsRate(),
                FwdPacketsRate(),
                DownUpRate(),

                AvgFwdBytesPerBulk(),
                AvgFwdPacketsPerBulk(),
                AvgFwdBulkRate(),
                AvgBwdBytesPerBulk(),
                AvgBwdPacketsPerBulk(),
                AvgBwdBulkRate(),
                FwdBulkStateCount(),
                FwdBulkSizeTotal(),
                FwdBulkPacketCount(),
                FwdBulkDuration(),
                BwdBulkStateCount(),
                BwdBulkSizeTotal(),
                BwdBulkPacketCount(),
                BwdBulkDuration(),

                FINFlagCounts(),
                PSHFlagCounts(),
                URGFlagCounts(),
                ECEFlagCounts(),
                SYNFlagCounts(),
                ACKFlagCounts(),
                CWRFlagCounts(),
                RSTFlagCounts(),
                FwdFINFlagCounts(),
                FwdPSHFlagCounts(),
                FwdURGFlagCounts(),
                FwdECEFlagCounts(),
                FwdSYNFlagCounts(),
                FwdACKFlagCounts(),
                FwdCWRFlagCounts(),
                FwdRSTFlagCounts(),
                BwdFINFlagCounts(),
                BwdPSHFlagCounts(),
                BwdURGFlagCounts(),
                BwdECEFlagCounts(),
                BwdSYNFlagCounts(),
                BwdACKFlagCounts(),
                BwdCWRFlagCounts(),
                BwdRSTFlagCounts(),

                FINFlagPercentageInTotal(),
                PSHFlagPercentageInTotal(),
                URGFlagPercentageInTotal(),
                ECEFlagPercentageInTotal(),
                SYNFlagPercentageInTotal(),
                ACKFlagPercentageInTotal(),
                CWRFlagPercentageInTotal(),
                RSTFlagPercentageInTotal(),
                FwdFINFlagPercentageInTotal(),
                FwdPSHFlagPercentageInTotal(),
                FwdURGFlagPercentageInTotal(),
                FwdECEFlagPercentageInTotal(),
                FwdSYNFlagPercentageInTotal(),
                FwdACKFlagPercentageInTotal(),
                FwdCWRFlagPercentageInTotal(),
                FwdRSTFlagPercentageInTotal(),
                BwdFINFlagPercentageInTotal(),
                BwdPSHFlagPercentageInTotal(),
                BwdURGFlagPercentageInTotal(),
                BwdECEFlagPercentageInTotal(),
                BwdSYNFlagPercentageInTotal(),
                BwdACKFlagPercentageInTotal(),
                BwdCWRFlagPercentageInTotal(),
                BwdRSTFlagPercentageInTotal(),
                FwdFINFlagPercentageInFwdPackets(),
                FwdPSHFlagPercentageInFwdPackets(),
                FwdURGFlagPercentageInFwdPackets(),
                FwdECEFlagPercentageInFwdPackets(),
                FwdSYNFlagPercentageInFwdPackets(),
                FwdACKFlagPercentageInFwdPackets(),
                FwdCWRFlagPercentageInFwdPackets(),
                FwdRSTFlagPercentageInFwdPackets(),
                BwdFINFlagPercentageInBwdPackets(),
                BwdPSHFlagPercentageInBwdPackets(),
                BwdURGFlagPercentageInBwdPackets(),
                BwdECEFlagPercentageInBwdPackets(),
                BwdSYNFlagPercentageInBwdPackets(),
                BwdACKFlagPercentageInBwdPackets(),
                BwdCWRFlagPercentageInBwdPackets(),
                BwdRSTFlagPercentageInBwdPackets(),

                PacketsIATMean(),
                PacketsIATStd(),
                PacketsIATMax(),
                PacketsIATMin(),
                PacketsIATSum(),
                PacketsIATMedian(),
                PacketsIATSkewness(),
                PacketsIATCoV(),
                PacketsIATMode(),
                PacketsIATVariance(),
                FwdPacketsIATMean(),
                FwdPacketsIATStd(),
                FwdPacketsIATMax(),
                FwdPacketsIATMin(),
                FwdPacketsIATSum(),
                FwdPacketsIATMedian(),
                FwdPacketsIATSkewness(),
                FwdPacketsIATCoV(),
                FwdPacketsIATMode(),
                FwdPacketsIATVariance(),
                BwdPacketsIATMean(),
                BwdPacketsIATStd(),
                BwdPacketsIATMax(),
                BwdPacketsIATMin(),
                BwdPacketsIATSum(),
                BwdPacketsIATMedian(),
                BwdPacketsIATSkewness(),
                BwdPacketsIATCoV(),
                BwdPacketsIATMode(),
                BwdPacketsIATVariance(),

                SubflowFwdPackets(),
                SubflowBwdPackets(),
                SubflowFwdBytes(),
                SubflowBwdBytes(),

                DeltaStart(),
                HandshakeDuration(),
                HandshakeState(),

                PacketsDeltaTimeMin(),
                PacketsDeltaTimeMax(),
                PacketsDeltaTimeMean(),
                PacketsDeltaTimeMode(),
                PacketsDeltaTimeVariance(),
                PacketsDeltaTimeStd(),
                PacketsDeltaTimeMedian(),
                PacketsDeltaTimeSkewness(),
                PacketsDeltaTimeCoV(),
                BwdPacketsDeltaTimeMin(),
                BwdPacketsDeltaTimeMax(),
                BwdPacketsDeltaTimeMean(),
                BwdPacketsDeltaTimeMode(),
                BwdPacketsDeltaTimeVariance(),
                BwdPacketsDeltaTimeStd(),
                BwdPacketsDeltaTimeMedian(),
                BwdPacketsDeltaTimeSkewness(),
                BwdPacketsDeltaTimeCoV(),
                FwdPacketsDeltaTimeMin(),
                FwdPacketsDeltaTimeMax(),
                FwdPacketsDeltaTimeMean(),
                FwdPacketsDeltaTimeMode(),
                FwdPacketsDeltaTimeVariance(),
                FwdPacketsDeltaTimeStd(),
                FwdPacketsDeltaTimeMedian(),
                FwdPacketsDeltaTimeSkewness(),
                FwdPacketsDeltaTimeCoV(),

                PacketsDeltaLenMin(),
                PacketsDeltaLenMax(),
                PacketsDeltaLenMean(),
                PacketsDeltaLenMode(),
                PacketsDeltaLenVariance(),
                PacketsDeltaLenStd(),
                PacketsDeltaLenMedian(),
                PacketsDeltaLenSkewness(),
                PacketsDeltaLenCoV(),
                BwdPacketsDeltaLenMin(),
                BwdPacketsDeltaLenMax(),
                BwdPacketsDeltaLenMean(),
                BwdPacketsDeltaLenMode(),
                BwdPacketsDeltaLenVariance(),
                BwdPacketsDeltaLenStd(),
                BwdPacketsDeltaLenMedian(),
                BwdPacketsDeltaLenSkewness(),
                BwdPacketsDeltaLenCoV(),
                FwdPacketsDeltaLenMin(),
                FwdPacketsDeltaLenMax(),
                FwdPacketsDeltaLenMean(),
                FwdPacketsDeltaLenMode(),
                FwdPacketsDeltaLenVariance(),
                FwdPacketsDeltaLenStd(),
                FwdPacketsDeltaLenMedian(),
                FwdPacketsDeltaLenSkewness(),
                FwdPacketsDeltaLenCoV(),

                HeaderBytesDeltaLenMin(),
                HeaderBytesDeltaLenMax(),
                HeaderBytesDeltaLenMean(),
                HeaderBytesDeltaLenMode(),
                HeaderBytesDeltaLenVariance(),
                HeaderBytesDeltaLenStd(),
                HeaderBytesDeltaLenMedian(),
                HeaderBytesDeltaLenSkewness(),
                HeaderBytesDeltaLenCoV(),
                BwdHeaderBytesDeltaLenMin(),
                BwdHeaderBytesDeltaLenMax(),
                BwdHeaderBytesDeltaLenMean(),
                BwdHeaderBytesDeltaLenMode(),
                BwdHeaderBytesDeltaLenVariance(),
                BwdHeaderBytesDeltaLenStd(),
                BwdHeaderBytesDeltaLenMedian(),
                BwdHeaderBytesDeltaLenSkewness(),
                BwdHeaderBytesDeltaLenCoV(),
                FwdHeaderBytesDeltaLenMin(),
                FwdHeaderBytesDeltaLenMax(),
                FwdHeaderBytesDeltaLenMean(),
                FwdHeaderBytesDeltaLenMode(),
                FwdHeaderBytesDeltaLenVariance(),
                FwdHeaderBytesDeltaLenStd(),
                FwdHeaderBytesDeltaLenMedian(),
                FwdHeaderBytesDeltaLenSkewness(),
                FwdHeaderBytesDeltaLenCoV(),

                PayloadBytesDeltaLenMin(),
                PayloadBytesDeltaLenMax(),
                PayloadBytesDeltaLenMean(),
                PayloadBytesDeltaLenMode(),
                PayloadBytesDeltaLenVariance(),
                PayloadBytesDeltaLenStd(),
                PayloadBytesDeltaLenMedian(),
                PayloadBytesDeltaLenSkewness(),
                PayloadBytesDeltaLenCoV(),
                BwdPayloadBytesDeltaLenMin(),
                BwdPayloadBytesDeltaLenMax(),
                BwdPayloadBytesDeltaLenMean(),
                BwdPayloadBytesDeltaLenMode(),
                BwdPayloadBytesDeltaLenVariance(),
                BwdPayloadBytesDeltaLenStd(),
                BwdPayloadBytesDeltaLenMedian(),
                BwdPayloadBytesDeltaLenSkewness(),
                BwdPayloadBytesDeltaLenCoV(),
                FwdPayloadBytesDeltaLenMin(),
                FwdPayloadBytesDeltaLenMax(),
                FwdPayloadBytesDeltaLenMean(),
                FwdPayloadBytesDeltaLenMode(),
                FwdPayloadBytesDeltaLenVariance(),
                FwdPayloadBytesDeltaLenStd(),
                FwdPayloadBytesDeltaLenMedian(),
                FwdPayloadBytesDeltaLenSkewness(),
                FwdPayloadBytesDeltaLenCoV(),
            ]

    def execute(self, data: list, data_lock, flows: List[Flow], features_ignore_list: list = [],
            label: str = "") -> list:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            self.__extracted_data = []
            for flow in flows:
                features_of_flow = {}
                features_of_flow["flow_id"] = str(flow)
                features_of_flow["timestamp"] = datetime.fromtimestamp(float(flow.get_timestamp()))
                features_of_flow["src_ip"] = flow.get_src_ip()
                features_of_flow["src_port"] = flow.get_src_port()
                features_of_flow["dst_ip"] = flow.get_dst_ip()
                features_of_flow["dst_port"] = flow.get_dst_port()
                features_of_flow["protocol"] = flow.get_protocol()
                feature: Feature
                for feature in self.__features:
                    if feature.name in features_ignore_list:
                        continue
                    feature.set_floating_point_unit(self.floating_point_unit)
                    try:
                        features_of_flow[feature.name] = feature.extract(flow)
                    except Exception as e:
                        print(f">>> Error occured in extracting the '{feature.name}' for '{flow}' flow.")
                        print(f">>> Error message: {e}")
                        print(110*"=")
                        features_of_flow[feature.name] = None
                        continue
                features_of_flow["label"] = label
                self.__extracted_data.append(features_of_flow.copy())
                # print(len(features_of_flow))
            with data_lock:
                data.extend(self.__extracted_data)
