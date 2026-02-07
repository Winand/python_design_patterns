import argparse
from abc import ABC, abstractmethod
from pathlib import Path
from typing import override


class VideoExporter(ABC):
    "Basic representation of video exporting codec."

    @abstractmethod
    def prepare_export(self, video_data: bytes) -> None:
        "Prepare video data for exporting."

    @abstractmethod
    def do_export(self, folder: Path) -> None:
        "Export the video data to a folder."


class LosslessVideoExporter(VideoExporter):
    "Lossless video exporting codec."

    @override
    def prepare_export(self, video_data: bytes) -> None:
        print("Preparing video data for lossless export.")

    @override
    def do_export(self, folder: Path) -> None:
        print(f"Exporting video data in lossless format to '{folder}'.")


class H264BPVideoExporter(VideoExporter):
    "H.264 video exporting codec with Baseline profile."

    @override
    def prepare_export(self, video_data: bytes) -> None:
        print("Preparing video data for H.264 (Baseline) export.")

    @override
    def do_export(self, folder: Path) -> None:
        print(f"Exporting video data in H.264 (Baseline) format to '{folder}'.")


class H264Hi422PVideoExporter(VideoExporter):
    "H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."

    @override
    def prepare_export(self, video_data: bytes) -> None:
        print("Preparing video data for H.264 (Hi422P) export.")

    @override
    def do_export(self, folder: Path) -> None:
        print(f"Exporting video data in H.264 (Hi422P) format to '{folder}'.")


class AudioExporter(ABC):
    "Basic representation of audio exporting codec."

    @abstractmethod
    def prepare_export(self, audio_data: bytes) -> None:
        "Prepare audio data for exporting."

    @abstractmethod
    def do_export(self, folder: Path) -> None:
        "Export the audio data to a folder."


class AACAudioExporter(AudioExporter):
    "AAC audio exporting codec."

    @override
    def prepare_export(self, audio_data: bytes) -> None:
        print("Preparing audio data for AAC export.")

    @override
    def do_export(self, folder: Path) -> None:
        print(f"Exporting audio data in AAC format to '{folder}'.")


class WAVAudioExporter(AudioExporter):
    "WAV (lossless) audio exporting codec."

    @override
    def prepare_export(self, audio_data: bytes) -> None:
        print("Preparing audio data for WAV export.")

    @override
    def do_export(self, folder: Path) -> None:
        print(f"Exporting audio data in WAV format to '{folder}'.")


class ExporterFactory(ABC):
    """
    Factory that represents a combination of video and audio codecs.

    The factory doesn't store the instances it created.
    """

    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        "Return a new video exporter instance."

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        "Return a new audio exporter instance."


class FastExporter(ExporterFactory):
    "High speed, lower quality audio and video export."

    @override
    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    @override
    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    "Slower speed, high quality audio and video export."

    @override
    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    @override
    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    "Low speed, master quality audio and video export."

    @override
    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    @override
    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def parse_arguments() -> argparse.Namespace:
    "Parse command line arguments."
    # read the desired export quality
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--quality",
        "-q",
        choices=["low", "high", "master"],
        required=True,
    )
    return parser.parse_args()


def to_exporter(export_quality: str) -> ExporterFactory:
    """
    Construct an exporter factory based on the given quality as a string.

    This is implemented as a Simple Factory coding idiom.
    """
    factories = {
        "low": FastExporter,
        "high": HighQualityExporter,
        "master": MasterQualityExporter,
    }
    if export_quality in factories:
        return factories[export_quality]()
    msg = f"Unknown output quality option: {export_quality}"
    raise ValueError(msg)


def main(fac: ExporterFactory) -> None:
    "Try out the Abstract Factory pattern."
    print("Hello from factory!")

    # retrieve the video and audio exporters
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export(b"placeholder_for_video_data")
    audio_exporter.prepare_export(b"placeholder_for_audio_data")

    # do the export
    folder = Path("./export")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    args = parse_arguments()
    fac = to_exporter(args.quality)
    main(fac)
